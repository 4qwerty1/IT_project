<template>
  <div id="home">
    <v-container class="d-flex align-self-center pb-0">
      <div>
        <v-text-field label="Поиск" solo class="d-inline-block mr-1" style="width: 400px" v-model="searchReq"
                      maxlength="100" cunter="100"/>
        <v-btn @click="search" class="ml-1">Поиск</v-btn>
      </div>

      <v-spacer/>

      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" rounded v-on="on">Создать обсуждение</v-btn>
        </template>

        <v-card>
          <v-text-field label="Название" placeholder="Название" solo class="pa-3 pb-0" maxlength="100" counter="100"
                        :error-messages="createTopicErrors" v-model="newTopicName"/>

          <v-card-actions class="text-center">
            <v-btn color="primary" @click="createTopicClick">Создать</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
    <view-topic v-for="topic in getTopics" :key="topic.id" :topic="topic"/>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import {required} from 'vuelidate/lib/validators'
import ViewTopicComponent from "@/components/ViewTopicComponent";

export default {
  name: "TopicsViewPage",
  components: {
    'view-topic': ViewTopicComponent
  },
  data() {
    return {
      dialog: false,
      searchReq: null,
      newTopicName: null
    }
  },
  validations: {
    newTopicName: {
      required
    }
  },
  computed: {
    ...mapGetters(['getTopics']),
    createTopicErrors() {
      let mess = ''
      if (!this.$v.newTopicName.$dirty) return mess
      if (!this.$v.newTopicName.required) mess = 'Введите название'

      return mess
    }
  },
  methods: {
    ...mapActions(['fetchTopics']),
    createTopic() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      this.axios.post('api/topics/', {title: this.newTopicName}, conf)
          .then(res => {
            if (res.statusText === 'Created') {
              this.$router.push({name: 'topic', query: {id: res.data.id}})
            }
          })

      this.dialog = false
    },
    createTopicClick() {
      this.$v.newTopicName.$touch()

      if (!this.$v.newTopicName.$invalid) {
        this.createTopic()
      }
    },
    search() {

    },
  },
  mounted() {
    this.fetchTopics()
  }
}
</script>

<style scoped>

</style>