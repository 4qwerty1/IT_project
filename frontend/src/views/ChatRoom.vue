<template>
  <div>
    <ChatView class="mw-600 container"></ChatView>
    <ChatTextField></ChatTextField>
  </div>
</template>

<script lang="js">
import ChatTextField from "../components/ChatTextField";
import ChatView from "../components/ChatView";

export default {
  name: "ChatRoom",
  components: {
    ChatTextField,
    ChatView
  },
}
</script>

<style lang="scss" scoped>

</style>