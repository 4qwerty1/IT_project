<template>
  <form class="container mw-400" novalidate @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Профиль</div>
      </md-card-header>

      <md-card-content>

        <ImageCropper @avatar="setAvatar"/>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('firstName')">
              <label for="firstName">Имя</label>
              <md-input id="firstName" v-model="form.firstName" autocomplete="given-name"
                        name="firstName"/>
              <span v-if="!$v.form.firstName.maxLength" class="md-error">Имя слишком длинное</span>
            </md-field>
          </div>
        </div>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('lastName')">
              <label for="lastName">Фамилия</label>
              <md-input id="lastName" v-model="form.lastName" autocomplete="given-name"
                        name="lastName"/>
              <span v-if="!$v.form.lastName.maxLength" class="md-error">Фамилия слишком длинная</span>
            </md-field>
          </div>
        </div>

        <md-button style="border-radius: 20px; width: 200px" class="md-raised md-primary" type="submit">Обновить
        </md-button>

        <md-snackbar :md-active.sync="userSaved">Данные пользователя обнавлены</md-snackbar>
      </md-card-content>
    </md-card>
  </form>
</template>

<script lang="js">
import axios from 'axios'
import {minLength, maxLength,} from 'vuelidate/lib/validators'
import ImageCropper from "@/components/ImageCropper";

export default {
  name: "Profile",
  components: {ImageCropper},
  data: () => ({
    form: {
      firstName: null,
      lastName: null,
      avatar: null
    },
    userSaved: false,
  }),
  validations: {
    form: {
      firstName: {
        minLength: minLength(3),
        maxLength: maxLength(50),
      },
      lastName: {
        minLength: minLength(3),
        maxLength: maxLength(50),
      }
    }
  },
  methods: {
    getValidationClass(fieldName) {
      const field = this.$v.form[fieldName]

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        };
      }
    },
    setAvatar(avatar) {
      this.form.avatar = avatar
      console.log(this.form.avatar)
    },
    async sendUser() {
      const user = {}
      if (this.form.firstName) {
        user['first_name'] = this.form.firstName
      }

      if (this.form.lastName) {
        user['last_name'] = this.form.lastName
      }

      if (this.form.avatar) {
        console.log(this.form.avatar)
        // user['avatar'] = this.form.avatar
      }
      const config = {
        headers: {
          Authorization: 'JWT ' + this.$cookies.get('token')
        }
      }

      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      await http.patch(`/api/profile`, user, config)
          .then(res => {
            if (res.statusText === 'Created')
              this.userSaved = true
          })
          .catch(err => {
            console.log(err.response)
          })
      if (this.userSaved)
        window.setTimeout(() => this.userSaved = false, 1500)

    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.sendUser()
      }
    },
  },
  async created() {
    const config = {headers: {Authorization: 'JWT ' + this.$cookies.get('token')}}

    const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
    await http.get('api/profile', config)
        .then(res => {
          if (res.status === 200) {
            this.firstName = res.data['first_name']
            this.lastName = res.data['lastName']
          }
        })
  }
}
</script>

<style scoped>

</style>