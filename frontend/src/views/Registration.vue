<template>
  <form class="container mw-400" novalidate @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Регистрация</div>
      </md-card-header>

      <md-card-content>
        <span v-if="this.invalidUser" class="md-body-1 error">Пользователь с таким именем уже существует</span>

        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('login')">
            <label for="login">Логин</label>
            <md-input id="login" v-model="form.login" autocomplete="given-name"
                      name="first-name" @click="crutch"/>
            <span v-if="!$v.form.login.required" class="md-error">Введите логин</span>
            <span v-else-if="!$v.form.login.ruLetter" class="md-error">
                Логин не должен содержать русских букв
            </span>
            <span v-else-if="!$v.form.login.minLength" class="md-error">Логин должен быть меньше 3 символов</span>
            <span v-else-if="!$v.form.login.maxlength" class="md-error">Логин должен быть больше 20 символов</span>
          </md-field>
        </div>

        <!--        <md-field :class="getValidationClass('email')">-->
        <!--          <label for="email">Email</label>-->
        <!--          <md-input id="email" v-model="form.email" autocomplete="email" name="email"-->
        <!--                    type="email"/>-->
        <!--          <span v-if="!$v.form.email.required" class="md-error">Введите email</span>-->
        <!--          <span v-else-if="!$v.form.email.email" class="md-error">Неверный email</span>-->
        <!--        </md-field>-->

        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('password')">
            <label for="password">Пароль</label>
            <md-input id="password" v-model="form.password" autocomplete="password" name="password"
                      type="password" @click="crutch"></md-input>
            <span v-if="!$v.form.password.required" class="md-error">Введите пароль</span>
            <span v-else-if="!$v.form.password.minLength" class="md-error">
              Минимальная длина пароля: 4 символа
            </span>
            <span v-else-if="!$v.form.password.ruLetter" class="md-error">
              Пароль не должен содержать русских букв
            </span>
          </md-field>
        </div>
      </md-card-content>

      <md-card-actions>
        <md-button class="md-primary" type="submit">Создать</md-button>
      </md-card-actions>

      <router-link class="rout-nav" to="login">Вход</router-link>

    </md-card>

    <md-snackbar :md-active.sync="userSaved">Пользователь {{ form.login }} успешно создан!</md-snackbar>
  </form>
</template>

<script lang="js">
import {validationMixin} from 'vuelidate'
import axios from 'axios'
import {maxLength, minLength, required,} from 'vuelidate/lib/validators'

export default {
  name: 'Registration',
  mixins: [validationMixin],
  data: () => ({
    form: {
      login: null,
      password: null
    },
    userSaved: false,
    invalidUser: false
  }),
  validations: {
    form: {
      login: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(20),
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      password: {
        required,
        minLength: minLength(4),
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)), // можно присваивать свои функции
      }
    },
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
      const user = {
        username: this.form.login,
        password: this.form.password
      }

      const http = axios.create({baseURL: 'http://localhost:8000/'});
      http.post(`/auth/users/`, user)
          .catch(err => {
            if (err.response.data.username[0]) {
              this.invalidUser = true
            }
          })

      if (!this.invalidUser) {
        this.userSaved = true
        window.setTimeout(() => this.$router.push({name: 'Login'}),
            1500)
      }
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.saveUser()
      }
    },
    crutch: () => this.invalidUser = false,
  }
}
</script>

<style lang="scss" scoped>
</style>