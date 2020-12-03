<template>
  <div class="home">

    <UserName ref="username"></UserName>

    <button style="margin-top: 10px" @click="login">Вход</button>
    <button style="margin-top: 10px" @click="reg">Регистрация</button>

  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import store from '../store'
import UserName from '../components/UserName.vue'
import axios from "axios";

@Options({
  components: {
    UserName,
  },
  methods: {
    login() {
      const err = this.validate();
      if (!err) return;

      const http = axios.create({baseURL: 'http://localhost:8000/form/'});
      http.get(`/api/users/?username=${this.$refs.username.username}`)
          .then((response) => {
            if (response.data.length != 0) {
              alert('all good');
            } else {
              alert('no this user in table');

            }
          });
    },
    reg() {
      // this.$router.push('Home');
      this.$router.push('register');
    },
    validate() {
      const err = !this.$refs.username.validate();
      return !err;
    }
  }
})



export default class Start extends Vue {

}
</script>

<style scoped>

</style>