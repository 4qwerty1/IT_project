<template>
  <div>
    <label>
      <select v-model="this.$store.state.favptrn">
        <option>Любимый pattern</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>Я гуманитарий</option>
      </select>
    </label>
  </div>
</template>

<script>
export default {
  name: "FavPtrn"
}
</script>

<style scoped>
div{
  padding-top: 10px;
}
</style>