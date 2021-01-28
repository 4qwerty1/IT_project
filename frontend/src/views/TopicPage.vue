<template>
  <div id="topic">
    <v-col class="ma-auto" cols="12" lg="8" md="10" sm="12">
      <view-messages :messages="getMessages" class="mb-3" id="view-messages"/>

      <div class="pos-relative">
        <v-textarea label="Сообщение" counter="200" no-resize outlined rows="4"
                    :error-messages="messageErrors"
                    class="round" v-model="message"
                    @keydown.enter.prevent="send"/>
        <v-btn class="send-btn" icon @click="trySend">
          <v-icon>mdi-send</v-icon>
        </v-btn>
      </div>
    </v-col>

    <v-snackbar top v-model="unAuthorized">Войдите, чтобы отправить сообщение</v-snackbar>
  </div>
</template>

<script>
import {required, maxLength} from 'vuelidate/lib/validators'
import {mapGetters, mapActions} from 'vuex'
import ViewMessagesComponent from '@/components/ViewMessagesComponent'

export default {
  name: "TopicPage",
  components: {
    'view-messages': ViewMessagesComponent
  },
  data() {
    return {
      message: null,
      topicID: null,
      unAuthorized: false,
      interval: null,
    }
  },
  validations: {
    message: {
      required,
      maxLength: maxLength(200)
    }
  },
  computed: {
    ...mapGetters(['getMessages']),
    messageErrors() {
      let mess = ''
      if (!this.$v.message.$dirty) return mess
      if (!this.$v.message.required) mess = ''
      if (!this.$v.message.maxLength) mess = 'Максимальная длина 200 символов'

      return mess
    }
  },
  methods: {
    ...mapActions(['fetchMessages', 'fetchNewMessages']),
    send() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      const mess = {
        topic: this.topicID,
        text: this.message
      }

      this.axios.post('api/messages/', mess, conf)
          .catch(err => {
            if (err.response.statusText === 'Unauthorized')
              this.unAuthorized = true
          })

      this.message = null
    },
    trySend() {
      this.$v.message.$touch()

      if (!this.$v.message.$invalid) {
        this.send()
      }
    },
  },
  async mounted() {
    this.topicID = this.$route.query.id
    await this.fetchMessages(this.topicID)

    const el = this.$el.querySelector('#view-messages')
    el.scrollTop = el.clientHeight

    this.interval = setInterval(() => {
      this.fetchNewMessages(this.topicID)
    }, 500)
  },
  beforeDestroy() {
    clearInterval(this.interval)
  },
}
</script>

<style scoped>

.pos-relative {
  position: relative;
}

.send-btn {
  position: absolute;
  bottom: 31px;
  right: 4px;
}

</style>