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
              <label for="login">Login</label>
              <md-input id="login" v-model="form.login" :disabled="sending" autocomplete="given-name"
                        name="login"/>
              <span v-if="!$v.form.login.required" class="md-error">Необходимо указать логин</span>
            </md-field>
          </div>

          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('password')">
              <label for="password">Пароль</label>
              <md-input id="password" v-model="form.password" autocomplete="password" name="password"
                        type="password"></md-input>
              <span v-if="!$v.form.password.required" class="md-error">Введите пароль</span>
            </md-field>
          </div>
        </div>
      </md-card-content>

      <md-progress-bar v-if="sending" md-mode="indeterminate"/>

      <md-card-actions>
        <md-button :disabled="sending" class="md-primary" type="submit">Войти</md-button>
      </md-card-actions>
      <router-link to="register">Зарегистрироваться</router-link>
    </md-card>
  </form>
</template>

<script lang="js">
import axios from 'axios';
import {required} from 'vuelidate/lib/validators';

// TODO убирать "неверный логин или пароль" при вводе
export default {
  name: "Login",
  data: () => ({
    form: {
      login: null,
      password: null
    },
    invalidUser: false,
    sending: false,
  }),
  validations: {
    form: {
      login: {
        required,
      },
      password: {
        required
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
    checkUser() {
      this.sending = true

      // TODO поправить запрос
      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      http.get(`/api/users/?login=${this.form.login}`)
          .then((response) => {
            if (response.data.length !== 0) {
              if (response.data[0].password === this.form.password) {
                console.log('ok');
              } else {
                this.invalidUser = true
              }
            } else {
              this.invalidUser = true
            }
            this.sending = false
          });
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.checkUser()
      }
    }
  }
}

</script>

<style lang="scss" scoped>

.error {
  color: #ff1744;
}

</style>