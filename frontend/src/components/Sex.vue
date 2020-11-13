<template>
  <div>
    <ul>
      <li><label><input name="sex" type="radio" value="male"
                        v-model="this.sex" @change="changeHandler">Муж</label></li>
      <li><label><input name="sex" type="radio" value="female"
                        v-model="this.sex" @change="changeHandler">Жен</label></li>
    </ul>
    <label v-if="this.error" style="color: crimson; display: block">Вы не выбрали пол</label>
  </div>
</template>

<script>
export default {
  name: "Sex",
  data() {
    return {
      sex: '',
      error: false,
    }
  },
  methods: {
    changeHandler() {
      this.validate();

      if (!this.error) {
        this.$store.state.sex = this.sex;
      } else {
        this.$store.state.sex = '';
      }
    },
    validate() {
      this.error = this.sex === '';

      return !this.error;
    }
  }
}
</script>

<style scoped>
ul {
  list-style: none;
  padding-left: 15px;
  margin-bottom: 0;
}

li {
  display: inline;
  padding-right: 20px;
}
</style>