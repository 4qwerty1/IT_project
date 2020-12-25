<template>
  <form class="container mw-400" novalidate @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Регистрация</div>
      </md-card-header>

      <md-card-content>
        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('login')">
            <label for="login">Логин</label>
            <md-input id="login" v-model="form.login" :disabled="sending" autocomplete="given-name"
                      name="first-name"/>
            <span v-if="!$v.form.login.required" class="md-error">Введите логин</span>
            <span v-else-if="!$v.form.login.minLength" class="md-error">Логин должен быть больше 3 символов</span>
            <span v-else-if="!$v.form.login.maxlength" class="md-error">Логин должен быть меньше 20 символов</span>
          </md-field>
        </div>

        <md-field :class="getValidationClass('email')">
          <label for="email">Email</label>
          <md-input id="email" v-model="form.email" :disabled="sending" autocomplete="email" name="email"
                    type="email"/>
          <span v-if="!$v.form.email.required" class="md-error">Введите email</span>
          <span v-else-if="!$v.form.email.email" class="md-error">Неверный email</span>
        </md-field>

        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('password')">
            <label for="password">Пароль</label>
            <md-input id="password" v-model="form.password" autocomplete="password" name="password"
                      type="password"></md-input>
            <span v-if="!$v.form.password.required" class="md-error">Введите пароль</span>
          </md-field>
        </div>
      </md-card-content>

      <md-progress-bar v-if="sending" md-mode="indeterminate"/>

      <md-card-actions>
        <md-button :disabled="sending" class="md-primary" type="submit">Создать</md-button>
      </md-card-actions>
    </md-card>

    <md-snackbar :md-active.sync="userSaved">Пользователь {{ form.login }} успешно создан!</md-snackbar>
  </form>
</template>

<script lang="js">
import {validationMixin} from 'vuelidate'
import axios from 'axios'
import {
  required,
  email,
  minLength,
  maxLength,
} from 'vuelidate/lib/validators'

export default {
  name: 'Registration',
  mixins: [validationMixin],
  data: () => ({
    form: {
      login: null,
      email: null,
      password: null
    },
    userSaved: false,
    sending: false,
    lastUser: null
  }),
  validations: {
    form: {
      login: {
        required,
        minLength: minLength(3),  // TODO проверить минимальное кол-во символов
        maxLength: maxLength(20)  // TODO проверить максимальное кол-во символов
      },
      email: {
        required,
        email
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
        }
      }
    },
    clearForm() {
      this.$v.$reset()
      this.form.login = null
      this.form.email = null
      this.form.password = null
    },
    saveUser() {
      this.sending = true

      const post = {
        'login': this.form.login,
        'access_right': 0,
        'password': this.form.password
      }

      const http = axios.create({baseURL: 'http://localhost:8000/'});
      http.post('/api/users/', post)
          .then((response) => {
            console.log(response)
            if (response.statusText === "Created") { // status code 201
              this.sending = false
              this.userSaved = true
            }
          })
          .catch((error) => {
            console.log(error);
          });
      // TODO проверять занят ли логин
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.saveUser()
      }
    },
  }
}
</script>

<style lang="scss" scoped>
</style>