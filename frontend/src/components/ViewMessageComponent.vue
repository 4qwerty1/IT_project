<template>
  <v-container class="align-self-center">
    <div class="msg-container">
      <span class="my-name">{{ message.name }}</span>
      <div class="left">
        <v-avatar style="background-color: #EEEEEE">
          <v-img :src="message.avatar"/>
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
          name: String,
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