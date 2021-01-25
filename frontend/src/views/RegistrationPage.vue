<template>
  <div id="registration">
    <v-form @submit.prevent="validateUser">
      <v-container class="mw-400">
        <v-card class="round" elevation="2">
          <v-card-title class="text-center">Регистрация</v-card-title>

          <span v-if="invalidUser" class="text-center error--text unselectable"
                style="position: absolute; text-align: center; left: 77px; top: 50px; max-width: 214px">
            Пользователь с таким логином уже существует
          </span>

          <v-container>
            <v-text-field v-model="user.username" :error-messages="usernameErrors"
                          label="Логин"
                          @keydown.space.prevent=""/> <!--@keydown.space.prevent - перехватывает пробел-->

            <v-text-field v-model="user.password" :error-messages="passwordErrors"
                          :type="showPassword ? 'text' : 'password'"
                          label="Пароль"
                          @keydown.space.prevent=""/>
            <v-btn icon style="position: absolute; left: auto; right: 10px; top: auto; bottom: 144px"
                   @click="showPassword = !showPassword">
              <v-icon>{{ showPassword ? 'mdi-eye' : 'mdi-eye-off' }}</v-icon>
            </v-btn>
          </v-container>
          <v-card-actions>
            <v-container class="text-center">
              <v-btn block class="rounded-pill primary" elevation="0" type="submit">Зарегистрироваться</v-btn>

              <div style="margin-top: 10px">
                <span>Уже зарегистрировались?</span>
                <router-link class="text-decoration-none blue--text text--darken-2 hover" to="/login">
                  Войти
                </router-link>
              </div>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-form>

    <v-snackbar top v-model="saved">Пользователь {{ user.username }} успешно создан</v-snackbar>
  </div>
</template>

<script>
import {required, minLength} from 'vuelidate/lib/validators';

export default {
  name: "RegistrationPage",
  data() {
    return {
      user: {
        username: null,
        email: null,
        password: null
      },
      showPassword: false,
      invalidUser: false,
      saved: false
    }
  },
  validations: {
    user: {
      username: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      password: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
        minLength: minLength(4)
      }
    }
  },
  computed: {
    usernameErrors() {
      let mess = ''
      if (!this.$v.user.username.$dirty) return mess
      if (!this.$v.user.username.required) mess = 'Введите логин'
      else if (!this.$v.user.username.ruLetter) mess = 'Логин не должен содержать русскх букв'

      return mess
    },
    passwordErrors() {
      let mess = ''
      if (!this.$v.user.password.$dirty) return mess
      if (!this.$v.user.password.required) mess = 'Введите пароль'
      else if (!this.$v.user.password.ruLetter) mess = 'Пароль не должен содержать русскх букв'
      else if (!this.$v.user.password.minLength) mess = 'Пароль должен быть не меньше 4 символов'

      return mess
    }
  },
  methods: {
    async sendUser() {
      await this.axios.post(`/auth/users/`, this.user)
          .then(res => {
            if (res.statusText === "Created") {
              this.saved = true;
            }
          })
          .catch((err) => {
            try {
              this.invalidUser = err.response.data.username[0].includes('already exists')
            } catch {
              this.invalidUser = false
            }
          })
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.sendUser()
      }
    }
  }
}
</script>

<style scoped>

</style>