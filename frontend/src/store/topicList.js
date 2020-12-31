import axios from "axios";

const http = axios.create({baseURL: 'http://localhost:8000/'});

export default {
    actions: {
        async fetchTopics(ctx) {
            const res = await http.get(`/api/topics`)
            ctx.commit('updateTopics', res.data)
        },
    },
    mutations: {
        updateTopics(state, topics) {
            state.topics = topics
        },
    },
    state: {
        topics: []
    },
    getters: {
        getTopics(state) {
            return state.topics
        }
    }
}