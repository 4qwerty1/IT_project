<template>
  <div>
    <label>
      <select v-model="this.favptrn" @change="changeHandler">
        <option>Любимый pattern</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>SOLID</option>
        <option>Я гуманитарий</option>
      </select>
    </label>
    <label class="invalid" v-if="this.error"
           style="color: crimson; display: block">Вы не выбрали любимый язык</label>
  </div>
</template>

<script>
export default {
  name: "FavPtrn",
  data() {
    return {
      favptrn: 'Любимый pattern',
      error: false,
    }
  },
  methods: {
    changeHandler() {
      this.validate();

      if (!this.error) {
        this.$store.state.favptrn = this.favptrn;
      } else {
        this.$store.state.favptrn = 'Любимый pattern';
      }
    },
    validate() {
      this.error = this.favptrn === 'Любимый pattern';
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