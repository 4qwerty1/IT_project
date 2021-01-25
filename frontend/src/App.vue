<template>
  <v-app class="bg-color">
    <NavbarComponent/>
    <router-view class="router fill-height"/>
  </v-app>
</template>

<script>
import '@/assets/styles/my-style.css'
import NavbarComponent from "@/components/NavbarComponent";

export default {
  name: 'App',
  components: {
    NavbarComponent
  },
};
</script>

<style lang="sass">
.bg-color
  background-color: #f5f5f5 !important

.router
  padding-top: 100px

</style>