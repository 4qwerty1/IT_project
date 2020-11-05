<template>
  <div>
    <label for="name">Имя</label>
    <input type="text" id="name" maxlength="15" placeholder="Имя"
           v-model="this.$store.state.name">
  </div>
</template>

<script>
export default {
  name: "Name",
  methods: {}
}
</script>

<style scoped>
label {
  display: block;
}

.in-valid {
  background: #f34141;
}
</style>