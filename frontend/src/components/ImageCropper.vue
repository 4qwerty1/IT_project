<template>
  <div>
    <md-dialog :md-active.sync="showDialog" @close="resetImg" @md-clicked-outside="resetImg">
      <md-dialog-title class="container">Выберите файл</md-dialog-title>

      <cropper ref="cropper" v-if="this.img.src" class="mw-500 mh-500" :src="this.img.src"
               stencil-component="circle-stencil"
               :size-restrictions-algorithm="percentsRestriction"/>
      <!--TODO попробовать сделать прикольный круг-->

      <div v-else class="container h-500 w-500">
        <input ref="img" type="file" name="file" class="input-file" accept="image/*"
               @change="loadImage($event)">
        <md-button class="md-primary md-raised" @click="$refs.img.click()">Загрузить фото</md-button>
      </div>

      <md-dialog-actions>
        <md-button class="md-primary" @click="cancelClick">Отмена</md-button>
        <md-button class="md-primary" @click="saveClick">Сохранить</md-button>
      </md-dialog-actions>
    </md-dialog>

    <md-button class="md-primary md-raised" @click="showDialog = true">Сменить аватарку</md-button>
  </div>
</template>

<script lang="js">
import {Cropper} from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

export default {
  name: "ImageCropper",
  components: {
    Cropper,
  },
  data() {
    return {
      img: {
        src: null,
        height: null,
        width: null
      },
      res: null,
      showDialog: false
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

        const form = new FormData()
        form.append('avatar', input.files[0], input.files[0].name)
        console.log(form)
        this.send(form)
      }
    },
    resetImg() {
      this.img.src = null
      this.img.width = null
      this.img.height = null
    },
    cancelClick() {
      this.showDialog = false
      this.resetImg()
    },
    saveClick() {
      const {canvas} = this.$refs.cropper.getResult();
      if (!canvas) {
        const form = new FormData();
        canvas.toBlob(blob => {
          form.append("image", blob);
          this.send(form)
        },);
        this.$emit('avatar', form)
      }
      this.showDialog = false
      // this.resetImg()
      // const form = new FormData();
      // canvas.toBlob(blob => {
      //   form.append("data", blob);
      // }, 'image/png')
      // console.log(form)
      // this.img.src = form
    },

    async send(form) {
      const config = {
        headers: {
          Authorization: 'JWT ' + this.$cookies.get('token'),
          // 'Content-Type': 'multipart/form-data'
        }
      }

      await this.axios.patch(`http://127.0.0.1:8000/api/profile`, {avatar: form}, config)
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err.response)
          })
    }
  },
}

// TODO попытаться поправить приближение
</script>

<style lang="scss" scoped>

.mh-500 {
  max-height: 500px;
}

.h-500 {
  height: 500px;
}

.w-500 {
  width: 500px;
}


.input-title {
  width: 100%;
  height: 100%;
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