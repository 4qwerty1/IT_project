<template>
  <div class="home">
    <form @submit.prevent="sendClick" novalidate>

      <Name></Name>

      <SurName></SurName>

      <Sex></Sex>

      <FavLang></FavLang>

      <FavPtrn></FavPtrn>

      <button style="margin-top: 10px">Click me</button>
    </form>
  </div>

</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import store from '../store'
import Name from '../components/Name.vue'
import SurName from '../components/SurName.vue'
import Sex from '../components/Sex.vue'
import FavLang from '../components/FavLang.vue'
import FavPtrn from '../components/FavPtrn.vue'

@Options({
  components: {
    Name,
    SurName,
    Sex,
    FavLang,
    FavPtrn,
  },
  methods: {
    sendClick() {
      console.log('name: ' + store.state.name);
      console.log('surname: ' + store.state.surname);
      console.log('sex: ' + store.state.sex);
      console.log('favlang: ' + store.state.favlang);
      console.log('favptrn: ' + store.state.favptrn);
    }
  }
})
export default class Home extends Vue {

}
</script>
