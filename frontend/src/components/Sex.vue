<template>
  <div>
    <ul>
      <li><label><input name="sex" type="radio" value="male"
                        v-model="this.$store.state.sex">Муж</label></li>
      <li><label><input name="sex" type="radio" value="female"
                        v-model="this.$store.state.sex">Жен</label></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Sex"
}
</script>

<style scoped>
ul {
  list-style: none;
  padding-left: 15px;
}

li {
  display: inline;
  padding-right: 20px;
}
</style>