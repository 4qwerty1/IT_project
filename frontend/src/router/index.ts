import Vue from 'vue'
import VueRouter, {RouteConfig} from 'vue-router'

// Views
import Home from '../views/Home.vue'
import Registration from '../views/Registration.vue'
import Login from '../views/Login.vue'
import ChatRoom from '../views/ChatRoom.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Registration',
        component: Registration
    },
    {
        path: '/chat',
        name: 'Chat',
        component: ChatRoom
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
