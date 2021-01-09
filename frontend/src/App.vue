<template>
  <div id="app">
    <md-toolbar id="nav-bar" class="c-dark" md-elevation="2"
                style="min-height: 48px !important; margin-bottom: 20px !important;">
      <div v-if="!isAuthorized" style="margin-left: auto; margin-right: 5%">
        <md-button class="md-raised md-primary round" @click="loginClick">Login</md-button>
        <md-button class="md-raised md-primary round" @click="registerClick">Registration</md-button>
      </div>
      <md-button v-else class="md-icon-button" style="margin-left: auto; margin-right: 5%"
                 type="button" @click="profileClick">
        <img class="icon" alt="send" src="./assets/icons/user.svg">
      </md-button>
    </md-toolbar>
    <router-view/>
  </div>
</template>

<script lang="js">
import './styles/my-style.scss'
import cookies from 'vue-cookies-reactive'
import router from "@/router";

export default {
  name: 'App',
  computed: {
    isAuthorized: () => cookies.isKey('token')
  },
  methods: {
    loginClick: () => router.push({name: 'Login'}),
    registerClick: () => router.push({name: 'Registration'}),
    profileClick: () => router.push({name: 'Profile'})
  }
}
</script>

<style lang="scss">
body {
  background-color: #edeef0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

::selection {
  background-color: #448aff !important;
}
</style>
