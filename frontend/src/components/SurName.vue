<template>
  <div>
    <label for="surname">Фамилия</label>
    <input type="text" id="surname" maxlength="20" placeholder="Фамилия"
           v-model="this.$store.state.surname">
  </div>
</template>

<script>
export default {
  name: "SurName",
}
</script>

<style scoped>
div {
  padding-top: 10px;
}

label {
  display: block;
}
</style>