<template>
  <div>
    <label>
      <select v-model="this.$store.state.favlang">
        <option>Любимый ЯП</option>
        <option>C</option>
        <option>C++</option>
        <option>C++++ (aka C#)</option>
        <option>Python</option>
        <option>Java</option>
        <option>Я гуманитарий</option>
      </select>
    </label>
  </div>
</template>

<script>
export default {
  name: "FavLang"
}
</script>

<style scoped>

</style>