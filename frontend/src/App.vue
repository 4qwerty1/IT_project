<template>
  <div id="app">
    <md-toolbar id="nav-bar" class="c-dark" md-elevation="2"
                style="min-height: 48px !important; margin-bottom: 20px !important;">
      <div v-if="false" style="margin-left: auto; margin-right: 5%">
        <md-button class="md-raised md-primary round" @click="loginClick">Login</md-button>
        <md-button class="md-raised md-primary round" @click="registerClick">Registration</md-button>
      </div>
      <md-button v-else-if="true" class="md-icon-button" style="margin-left: auto; margin-right: 5%"
                 type="button" @click="profileClick">
        <img class="icon" alt="send" src="./assets/icons/user.svg">
      </md-button>
    </md-toolbar>
    <router-view/>
  </div>
</template>

<script lang="js">
import './styles/my-style.scss'

export default {
  name: 'App',
  methods: {
    loginClick() {
      this.$router.push({name: 'Login'})
    },
    registerClick() {
      this.$router.push({name: 'Registration'})
    },
    profileClick() {
      this.$router.push({name: 'Profile'})
    }
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
