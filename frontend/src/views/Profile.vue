<template>
  <div id="profile">
    <v-container class="mw-400">
      <v-card>
        <v-card-title class="text-center">Профиль</v-card-title>

        <v-row>
          <v-col cols="5" class="text-center pt-0">
            <v-avatar size="56" class="ma-2" style="background-color: #EEEEEE">
              <v-img :src="user.avatar"/>
            </v-avatar>
          </v-col>

          <!--TODO может убрать и сделать кликабельную аватарку?-->
          <v-col cols="5" class="text-center pt-0">

            <image-cropper :username="user.username" @avatar="user.avatar = $event"/>
            <!--            <v-btn color="primary" v-on="on">Сменить аватар</v-btn>-->
          </v-col>
        </v-row>

        <v-card-text>
          <v-row>
            <v-col class="pt-0">
              <v-text-field label="Логин" readonly :value="user.username"/>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pt-0">
              <v-text-field label="Имя" counter="30" maxlength="30" v-model="user.firstname"/>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pt-0">
              <v-text-field label="Фамилия" counter="30" maxlength="30" v-model="user.lastname"/>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions class="text-center">
          <v-btn color="primary" @click="saveClick">Сохранить изменения</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>

    <v-snackbar top v-model="updated">Данные пользователя обновлены</v-snackbar>
  </div>
</template>

<script>
import ImageCropper from "@/components/ImageCropper";

export default {
  name: "Profile",
  components: {ImageCropper},
  data() {
    return {
      user: {
        avatar: null,
        username: null,
        firstname: null,
        lastname: null,
      },
      updated: false,
    }
  },
  methods: {
    save() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      const user = {
        first_name: this.user.firstname,
        last_name: this.user.lastname
      }

      this.axios.patch('api/profile/', user, conf)
          .catch(err => console.log(err))

      this.updated = true
    },
    saveClick() {
      this.$v.user.$touch()

      if (!this.$v.user.$invalid) {
        this.save()
      }
    }
  },
  created() {
    const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    this.axios.get('api/profile/', conf)
        .then(res => {
          if (res.statusText === 'OK') {
            this.user.username = res.data.username
            this.user.firstname = res.data.first_name
            this.user.lastname = res.data.last_name
            this.user.avatar = res.data.avatar
          }
        })
  }
}
</script>

<style scoped>

</style>