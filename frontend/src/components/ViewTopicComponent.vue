<template>
  <v-container class="align-self-center">
    <div class="msg-container">
      <router-link :to="{name: 'topic', query: {id: topic.id}}"
                   class="my-title hover">{{ topic.title }}
      </router-link>

      <div class="left">
        <v-avatar>
          <img src="@/assets/icons/user.svg" alt="Ava">
        </v-avatar>
      </div>
      <div class="message-topic">{{ topic.text }}</div>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "ViewTopicComponent",
  props: {
    topic: {
      required: true,
      type: Object,
      default() {
        return {
          id: Number,
          title: String,
          text: String
        }
      }
    }
  }
}
</script>

<style scoped>

</style>