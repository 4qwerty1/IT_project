<template>
  <div id="chat-room">
    <ChatView class="mw-500 container" :messages="getPosts"></ChatView>
    <ChatTextField></ChatTextField>
  </div>
</template>

<script lang="js">
// TODO возможно, стоит добавить название топика

import ChatTextField from "../components/ChatTextField";
import ChatView from "../components/ChatView";
import {mapActions, mapGetters} from 'vuex';

export default {
  name: "ChatRoom",
  props: {
    topicId: {
      required: true, // TODO вернуть необходимость topicId
      type: Number,
    }
  },
  components: {
    ChatTextField,
    ChatView
  },
  computed: mapGetters(['getPosts']),
  methods: mapActions(['fetchPosts']),
  mounted() {
    this.fetchPosts(this.topicId)
  }
}
</script>

<style lang="scss" scoped>

</style>