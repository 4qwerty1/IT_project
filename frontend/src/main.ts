import {createApp} from 'vue'
import { validationMixin } from 'vuelidate'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(validationMixin).use(store).use(router).mount('#app')
