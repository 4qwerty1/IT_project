<template>
  <v-card class="round h-500 mh-500 scrollbar round-track">
    <view-message v-for="message in messages" :key="message.id" :message="message"/>
  </v-card>
</template>

<script>
import ViewMessageComponent from '@/components/ViewMessageComponent'

export default {
  name: "ViewMessagesComponent",
  components: {
    'view-message': ViewMessageComponent
  },
  props: {
    messages: {
      required: true,
      type: Array,
      default() {
        return [{
          id: Number,
          name: String,
          avatar: String,
          text: String,
        }]
      }
    }
  },
}
</script>

<style scoped>

.h-500 {
  height: 500px;
}

.mh-500 {
  max-height: 500px;
}

</style>