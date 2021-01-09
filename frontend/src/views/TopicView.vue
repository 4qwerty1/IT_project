<template>
  <md-content class="container md-scrollbar mw-500">
    <div class="msg-container topic" v-for="topic in getTopics" :key="topic.id">
      <router-link class="rout-nav" :to="{ name: 'Chat', params: { topicId: topic.id, topicTitle: topic.title }}">
        {{ topic.title }}
      </router-link>
    </div>
  </md-content>
</template>

<script lang="js">
import {mapActions, mapGetters} from 'vuex'

export default {
  name: "TopicView",
  computed: mapGetters(['getTopics']),
  methods: mapActions(['fetchTopics']),
  mounted() {
    this.fetchTopics()
  }
}
</script>

<style lang="scss" scoped>

.topic {
  margin: 10px;
}

.md-content {
  height: 70ex;
  overflow: auto;
}
</style>