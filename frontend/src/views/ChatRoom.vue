<template>
  <div id="chat-room">
    <div class="container" style="margin: 10px; font-size: 20px">{{ topicTitle }}</div>
    <ChatView class="mw-500 container" :messages="getPosts"></ChatView>
    <ChatTextField v-if="this.$cookies.isKey('token')" :topic-id="topicId"></ChatTextField>
  </div>
</template>

<script lang="js">

import ChatTextField from "../components/ChatTextField";
import ChatView from "../components/ChatView";
import {mapActions, mapGetters} from 'vuex';

export default {
  name: "ChatRoom",
  props: {
    topicTitle: {
      type: String,
      default: null
    },
    topicId: {
      type: Number,
      default: 0
    }
  },
  components: {
    ChatTextField,
    ChatView
  },
  computed: mapGetters(['getPosts']),
  methods: mapActions(['fetchPosts']),
  created() {
    if (this.topicId !== 0)
      this.fetchPosts(this.topicId)
  }
}
</script>

<style lang="scss" scoped>

</style>