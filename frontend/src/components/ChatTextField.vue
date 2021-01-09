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
import {mapActions, mapGetters} from 'vuex'


export default {
  name: "ChatTextField",
  props: {
    topicId: Number
  },
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
  computed: mapGetters(['getPosts']),
  methods: {
    ...mapActions(['updatePosts']),
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
    async sendMessage() {
      const message = {
        topic: this.topicId,
        text: this.message,
        sender: 26, // TODO REMOVE ME!
      }
      const config = {headers: {Authorization: 'JWT ' + this.$cookies.get('token')}}

      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      await http.post('api/create-message', message, config)
          .then((res) => {
            if (res.statusText === 'Created') {
              this.updatePosts(this.topicId, this.getPosts[this.getPosts.length - 1]['time_create'])
            }
          })
          .catch((err) => {
            console.log(err)
          })
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