<template>
  <v-container class="align-self-center">
    <div class="msg-container">
      <span class="my-name">{{ message.get_name }}</span>
      <div class="left">
        <v-avatar>
          <img :src="message.avatar" alt="Ava">
        </v-avatar>
      </div>
      <div class="message">{{ message.text }}</div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "ViewMessageComponent",
  props: {
    message: {
      required: true,
      type: Object,
      default() {
        return {
          get_name: String,
          avatar: String,
          text: String
        }
      }
    }
  },
}
</script>

<style lang="sass" scoped>
</style>