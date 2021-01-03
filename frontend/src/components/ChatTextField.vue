<template>
  <form class="container mw-400" novalidate @submit.prevent="validateMessage">
    <md-field :class="getValidationClass('message')">
      <label>Сообщение</label>
      <md-textarea class="mh-130" v-model="message" md-autogrow
                   :md-counter="$v.message.$params.maxLength.max"></md-textarea>
      <md-button class="md-icon-button" style="margin-top: auto" type="submit">
        <img class="icon" src="../assets/icons/send.svg" alt="send">
      </md-button>
      <span v-if="!$v.message.maxLength" class="md-error"> текст не может быть больше
        {{ $v.message.$params.maxLength.max }}</span>
    </md-field>
  </form>
</template>

<script lang="js">
import axios from 'axios';
import {maxLength, required,} from 'vuelidate/lib/validators';


export default {
  name: "ChatTextField",
  data() {
    return {
      message: null,
    }
  },
  validations: {
    message: {
      required,
      maxLength: maxLength(200)
    }
  },
  methods: {
    getValidationClass(fieldName) {
      const field = this.$v[fieldName]

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        };
      }
    },
    clearForm() {
      this.$v.$reset()
      this.message = null
    },
    sendMessage() {

      const message = {
        id: 2,
        firstname: 'excorador',
        icon: 'url',
        text: this.message
      }
      this.$store.dispatch('addPost', message)

      const post = {
        text: this.message,
        topic: 1,
        sender: 1,
      }
      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      http.post('api/messages/', post)
          .then((res) => {
            if (res.status === 200) {
              console.log(res.data[0])
            }
          })
          .catch((err) => {
            console.log(err)
          })

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

.mh-130 {
  max-height: 130px !important;
}

</style>