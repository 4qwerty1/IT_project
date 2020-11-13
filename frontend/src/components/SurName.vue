<template>
  <div>
    <label for="surname">Фамилия</label>
    <input type="text" id="surname" maxlength="20" placeholder="Фамилия"
           v-model="this.surname" @input="inputHandler" :class="{invalid : error}">
    <label class="invalid" v-if="this.error && !this.empty">В поле не должно быть цифр и спец символов</label>
    <label class="invalid" v-if="this.error && this.empty">Поле не должно быть пустым</label>
  </div>
</template>

<script>
export default {
  name: "SurName",
  data() {
    return {
      surname: '',
      error: false,
      touch: false,
      empty: false
    }
  },
  methods: {
    inputHandler() {
      this.validate();

      if (!this.error) {
        this.$store.state.surname = this.surname;
      } else {
        this.$store.state.surname = '';
      }
    },
    validate() {
      this.touch = true;
      const re = /[0-9/,.\\!@"#№$;%^:&?*()<>{}\-_+=~`\[\]|']/;
      const result = this.surname.match(re);

      this.error = result != null;
      if (this.touch && this.surname.length === 0) {
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
div {
  padding-top: 10px;
}

label {
  display: block;
}

.invalid {
  color: crimson;
  border-color: crimson;
}
</style>