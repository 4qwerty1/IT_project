<template>
  <v-dialog v-model="dialog" width="510">
    <template v-slot:activator="{ on }">
      <v-btn color="primary" v-on="on">Сменить аватар</v-btn>
    </template>

    <v-card>
      <cropper ref="cropper" v-if="img.src !== null" class="mh-500" :src="img.src"
               stencil-component="circle-stencil"
               :size-restrictions-algorithm="percentsRestriction"/>

      <v-container v-else class="text-center">
        <input ref="img" type="file" name="file" class="input-file" accept="image/*"
               @change="loadImage($event)">
        <v-btn @click="$refs.img.click()" color="primary">Загрузить фото</v-btn>
      </v-container>

      <v-card-actions class="text-center">
        <v-btn color="primary" @click="saveClick">Сохранить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import {Cropper} from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

export default {
  name: "ImageCropper",
  components: {
    Cropper,
  },
  props: {
    username: null
  },
  data() {
    return {
      img: {
        src: null,
        height: null,
        width: null
      },
      res: null,
      dialog: false,
    }
  },
  methods: {
    percentsRestriction() {
      return {
        minWidth: (this.img.width / 4),   // min stencil width  (also affects the magnification of the image)
        minHeight: (this.img.height / 4), // min stencil height (also ...)
        maxWidth: this.img.width,         // max stencil width  (also ...)
        maxHeight: this.img.height,       // max stencil height (also ...)
      };
    },
    loadImage(event) {
      const input = event.target;
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.img.src = e.target.result;
          const img = new Image;
          img.onload = () => {
            this.img.width = img.width
            this.img.height = img.height
          }

          img.src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
      }
    },
    saveClick() {
      const {canvas} = this.$refs.cropper.getResult();

      const conf = {
        headers: {
          Authorization: 'JWT ' + this.$cookies.get('Token'),
          'Content-Type': 'multipart/form-data'
        }
      }

      const data = new FormData()
      canvas.toBlob(blob => {
        data.append("avatar", blob, this.username + '.jpg'); // TODO maybe just avatar.jpg

        this.axios.patch('api/profile/', data, conf)
            .catch(err => console.log(err))
      }, 'image/jpg')

      this.$emit('avatar', canvas.toDataURL())
      this.dialog = false
    },
  },
}
</script>

<style scoped>

.mh-500 {
  max-height: 500px;
}

.input-file {
  width: 0;
  height: 0;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

</style>