import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


// input views
import TopicsViewPage from "@/views/TopicsViewPage"
import LoginPage from "@/views/LoginPage"
import RegistrationPage from "@/views/RegistrationPage"
import TopicPage from "@/views/TopicPage";
import Profile from "@/views/Profile";


const routes = [
    {
        path: '/',
        name: 'home',
        component: TopicsViewPage
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationPage
    },
    {
        path: '/topic',
        name: 'topic',
        component: TopicPage,
        beforeEnter(to, from, next) {
            if (to.query.id === undefined) next({name: 'home'})
            else next()
        }
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile,
        beforeEnter(to, from, next) {
            if (!Vue.$cookies.isKey('Token')) next({name: 'home'})
            else next()
        }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
