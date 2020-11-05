<template>
  <div class="home">
    <form novalidate>
    <pre>
      {{ this.$v.regForm.name }}
    </pre>

      <div>
        <input type="text" id="name" maxlength="15" placeholder="Имя"
               v-model="this.$store.state.regForm.name" @blur="this.$v.regForm.name.touch()">
      </div>

      <div style="margin-top: 10px">
        <input type="text" id="surname" maxlength="20" placeholder="Фамилия"
               v-model="this.$store.state.regForm.surname">
      </div>

      <div>
        <ul style="list-style: none; padding-left: 15px">
          <li style="display: inline; padding-right: 20px"><input name="sex" type="radio">Муж
          </li>
          <li style="display: inline; padding-right: 20px"><input name="sex" type="radio">Жен
          </li>
        </ul>
      </div>

      <div>
        <select v-model="this.$store.state.regForm.language">
          <option>Любимый ЯП</option>
          <option>C</option>
          <option>C++</option>
          <option>C++++ (aka C#)</option>
          <option>Python</option>
          <option>Java</option>
          <option>Я гуманитарий</option>
        </select>
      </div>

      <div style="margin: 10px">
        <select v-model="this.$store.state.regForm.pattern">
          <option>Любимый pattern</option>
          <option>SOLID</option>
          <option>SOLID</option>
          <option>SOLID</option>
          <option>Я гуманитарий</option>
        </select>
      </div>

      <button @click="sendClick">Click me</button>
    </form>
  </div>

</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import store from '../store'

@Options({
  components: {},
  methods: {
    sendClick() {
      console.log(store.getters.getForm);
    },

  },
  validations: {
    regForm: {
      name: {
        required: require
      }
    }
  }
})
export default class Home extends Vue {

}

</script>
