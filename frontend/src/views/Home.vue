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
      const err = this.validate();
      if (err) this.sendRequest();
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
      const http = axios.create({baseURL: 'http://localhost:8000/form/'});

      // http.get('/api/users/').then(response => {
      //   console.log(response.data);
      // })

      const post = {
        "firstName": this.$refs.name.name,
        "lastName": this.$refs.surname.surname,
        "sex": (this.$refs.sex.sex == "male"),
        "favPL": this.$refs.favlang.favlang,
        "favPattern": this.$refs.favptrn.favptrn
      }

      http.post('/api/users/', post)
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
    }
  }
})
export default class Home extends Vue {

}
</script>
