import axios from "axios";

const http = axios.create({baseURL: 'http://localhost:8000/'});

export default {
    actions: {
        async fetchPosts(ctx, topicId) {
            const res = await http.get(`/api/messages/?topic=${topicId}`)
            ctx.commit('updatePosts', res.data)
        },
        addPost(ctx, post) {
            ctx.commit('addPostMutation', post)
        }
    },
    mutations: {
        updatePosts(state, posts) {
            state.posts = posts
        },
        addPostMutation(state, post) {
            state.posts.push(post)
        }
    },
    state: {
        posts: []
    },
    getters: {
        getPosts(state) {
            return state.posts
        }
    }
}