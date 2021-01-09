<template>
  <form class="container mw-400" novalidate @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Вход</div>
      </md-card-header>

      <md-card-content>
        <span v-if="invalidUser" class="md-body-1 error">Неверный логин или пароль</span>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('login')">
              <label for="login">Логин</label>
              <md-input id="login" v-model="form.login" autocomplete="given-name"
                        name="login" @input="crutch"/>
              <span v-if="!$v.form.login.required" class="md-error">Необходимо указать логин</span>
              <span v-else-if="!$v.form.login.ruLetter" class="md-error">
                Логин не должен содержать русских букв
              </span>
            </md-field>
          </div>

          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('password')">
              <label for="password">Пароль</label>
              <md-input id="password" v-model="form.password" autocomplete="password" name="password"
                        type="password" @input="crutch"></md-input>
              <span v-if="!$v.form.password.required" class="md-error">Введите пароль</span>
              <span v-else-if="!$v.form.password.ruLetter" class="md-error">
                Пароль не должен содержать русских букв
              </span>

            </md-field>
          </div>
        </div>
      </md-card-content>

      <md-card-actions>
        <md-button class="md-primary" type="submit">Войти</md-button>
      </md-card-actions>
      <router-link class="rout-nav" to="register">Зарегистрироваться</router-link>
    </md-card>
  </form>
</template>

<script lang="js">
import axios from 'axios';
import {required} from 'vuelidate/lib/validators';

export default {
  name: "Login",
  data: () => ({
    form: {
      login: null,
      password: null
    },
    invalidUser: false,
  }),
  validations: {
    form: {
      login: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      password: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
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
    async checkUser() {
      const user = {
        username: this.form.login,
        password: this.form.password
      }

      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      await http.post(`/auth/jwt/create/`, user).then(
          res => {
            console.log(res)
            if (res.status === 200)
              this.$cookies.set('token', res.data.access)
          }
      ).catch(() => this.invalidUser = true)

      if (!this.invalidUser)
        window.setTimeout(() => this.$router.push({name: 'TopicView'}),
            500)
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.checkUser()
      }
    },
    crutch() {
      this.invalidUser = false
    }
  }
}

</script>

<style lang="scss" scoped>

.error {
  color: #ff1744;
}

</style>