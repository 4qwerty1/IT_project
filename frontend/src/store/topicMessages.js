import axios from "axios";

const http = axios.create({baseURL: 'http://localhost:8000/'});

export default {
    actions: {
        async fetchPosts(ctx, topicId) {
            const res = await http.get(`/api/get-messages/?topic=${topicId}`)
            ctx.commit('fetchPostsMutation', res.data)
        },
        async updatePosts(ctx, topicId, last) {
            console.log(topicId, last)
            // const posts = await http.get(`/api/load-messages/?topic=${topicId}&last_message=${last}`)
            // ctx.commit('updatePostsMutation', posts.data)
        }
    },
    mutations: {
        fetchPostsMutation(state, posts) {
            state.posts = posts
        },
        updatePostsMutation(state, posts) {
            // console.log(posts)
            posts.forEach((mess) => state.posts.push(mess))
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