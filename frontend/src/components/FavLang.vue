<template>
  <div>
    <label>
      <select v-model="this.favlang" @change="changeHandler">
        <option>Любимый ЯП</option>
        <option>C</option>
        <option>C++</option>
        <option>C++++ (aka C#)</option>
        <option>Python</option>
        <option>Java</option>
        <option>Я гуманитарий</option>
      </select>
    </label>
    <label v-if="this.error" style="color: crimson; display: block">Вы не выбрали любимый язык</label>
  </div>
</template>

<script>
export default {
  name: "FavLang",
  data() {
    return {
      favlang: 'Любимый ЯП',
      error: false,
    }
  },
  methods: {
    changeHandler() {
      this.validate();

      if (!this.error) {
        this.$store.state.favlang = this.favlang;
      } else {
        this.$store.state.favlang = '';
      }
    },
    validate() {
      this.error = this.favlang === 'Любимый ЯП';

      return !this.error;
    }
  }
}
</script>

<style scoped>
div {
  padding-top: 10px;
}
</style>