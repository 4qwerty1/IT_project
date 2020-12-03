<template>
  <div class="home">
    <form @submit.prevent="sendClick" novalidate>

      <Name ref="name"></Name>

      <SurName ref="surname"></SurName>

      <Sex ref="sex"></Sex>

      <FavLang ref="favlang"></FavLang>

      <FavPtrn ref="favptrn"></FavPtrn>

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
import axios from 'axios'

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
      this.sendRequest();
      const err = this.validate();
      if (err) alert("Всё ок!");
    },
    validate() {
      let err = !this.$refs.name.validate();
      err = !this.$refs.surname.validate() || err;
      err = !this.$refs.sex.validate() || err;
      err = !this.$refs.favlang.validate() || err;
      err = !this.$refs.favptrn.validate() || err;
      return !err;
    },
    sendRequest() {
      // this.axios.defaults.baseURL = '//127.0.0.1:8000/';
      // axios.get('//127.0.0.1:8000/api/orders/');
      // axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      axios.get('//127.0.0.1:8000/api/orders/') // отправит запрос на /api/orders
          .then((response) => {
            console.log('hello, motherfucker');
          }) // после того как придет ответ, получаем ответ от сервера
          .catch(function (error) {
            console.log("it's error, motherfucker!");
          });

      // axios
      //     .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      //     .then(response => (this.info = response))
      //     .catch(function (error) {
      //       console.log("it's error, motherfucker!");
      //     });
    }
  }
})
export default class Home extends Vue {

}
</script>
