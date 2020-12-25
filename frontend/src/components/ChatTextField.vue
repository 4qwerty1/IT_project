<template>
  <form class="container mw-400" novalidate @submit.prevent="validateMessage">
    <md-field :class="getValidationClass('message')">
      <label>Сообщение</label>
      <md-textarea v-model="form.message" md-autogrow md-counter="200"></md-textarea>
      <md-button class="md-icon-button" style="margin-top: auto" type="submit">
        <img src="../assets/icons/send.svg" alt="send" style="opacity: 60%">
      </md-button>
      <span v-if="!$v.form.message.maxLength" class="md-error"> текст не может быть больше
        {{ $v.form.message.maxLength }}</span>
    </md-field>
  </form>
</template>

<script lang="js">
import axios from 'axios';
import {
  required,
  maxLength,
} from 'vuelidate/lib/validators';


export default {
  name: "ChatTextField",
  data() {
    return {
      form: {
        message: null,
      },
      sending: false
    }
  },
  validations: {
    form: {
      message: {
        required,
        maxLength: maxLength(200)
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
    clearForm() {
      this.$v.$reset()
      this.form.message = null
    },
    sendMessage() {
      this.sending = true

      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      // TODO написать post запрос
    },
    validateMessage() {
      this.$v.$touch()

      // TODO проверка на пусткую строку
      if (!this.$v.$invalid) {
        this.sendMessage()
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>