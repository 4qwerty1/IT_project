import Vue from 'vue'
import VueRouter, {RouteConfig} from 'vue-router'

// import views
import Login from '@/views/Login.vue'
import Registration from '@/views/Registration.vue'
import Profile from '@/views/Profile.vue'
import ChatRoom from '@/views/ChatRoom.vue'
import TopicView from '@/views/TopicView.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'TopicView',
        component: TopicView
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
        props: true,
        component: ChatRoom,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
