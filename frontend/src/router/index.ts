import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Start from '../views/Start.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/register',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'Start',
    component: Start
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
