<template>
  <div>
    <label for="name">Имя</label>
    <input type="text" id="name" maxLength="15" placeholder="Имя"
           v-model="this.name" @input="inputHandler" :class="{invalid : error}">
    <label class="invalid" v-if="this.error && !this.empty">В поле не должно быть цифр и спец символов</label>
    <label class="invalid" v-if="this.error && this.empty">Поле не должно быть пустым</label>
  </div>
</template>

<script>
export default {
  name: "Name",
  data() {
    return {
      name: '',
      error: false,
      touch: false,
      empty: false
    }
  },
  methods: {
    inputHandler() {
      this.validate();

      if (!this.error) {
        this.$store.state.name = this.name;
      } else {
        this.$store.state.name = '';
      }
    },
    validate() {
      this.touch = true;
      const re = /[0-9/,.\\!@"#№$;%^:&?*()<>{}\-_+=~`\[\]|']/;
      const result = this.name.match(re);

      this.error = result != null;
      if (this.touch && this.name.length === 0) {
        this.error = true;
        this.empty = true;
      } else {
        this.empty = false;
      }

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