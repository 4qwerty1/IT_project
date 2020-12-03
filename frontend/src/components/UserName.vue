<template>
  <div>
    <label for="username">Имя пользователя</label>
    <input type="text" id="username" maxLength="50" placeholder="Имя пользователя"
           v-model="this.username" @input="inputHandler" :class="{invalid : error}">
    <label class="invalid" v-if="this.error">Поле не должно быть пустым</label>
  </div>
</template>

<script>
export default {
  name: "UserName",
  data() {
    return {
      username: '',
      error: false,
    }
  },
  methods: {
    inputHandler() {
      this.$store.state.username = this.username;
    },
    validate() {
      this.error = this.username.length === 0
      return !this.error;
    }
  }
}
</script>

<style scoped>
label {
  display: block;
}

.invalid {
  color: crimson;
  border-color: crimson;
}
</style>