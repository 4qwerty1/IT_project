<template>
  <form class="container mw-400" novalidate @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Профиль</div>
      </md-card-header>

      <md-card-content>

        <ImageCropper/>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('firstName')">
              <label for="firstName">Имя</label>
              <md-input id="firstName" v-model="form.firstName" :disabled="sending" autocomplete="given-name"
                        name="firstName"/>
            </md-field>
          </div>
        </div>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('lastName')">
              <label for="lastName">Фамилия</label>
              <md-input id="lastName" v-model="form.lastName" :disabled="sending" autocomplete="given-name"
                        name="lastName"/>
            </md-field>
          </div>
        </div>

      </md-card-content>
    </md-card>
  </form>
</template>

<script lang="js">
import axios from 'axios'
import {required, maxLength,} from 'vuelidate/lib/validators'
import ImageCropper from "@/components/ImageCropper";

export default {
  name: "Profile",
  components: {ImageCropper},
  data: () => ({
    form: {
      firstName: null,
      lastName: null
    },
    sending: false,
  }),
  validations: {
    form: {
      firstName: {
        required,
        maxLength: maxLength(50),
      },
      lastName: {
        required,
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
    sendUser() {
      this.sending = true

      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      // TODO написать запрос на замену данных
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.sendUser()
      }
    },
    // TODO добавить метод, заполнения полей
  }
}
</script>

<style scoped>

</style>