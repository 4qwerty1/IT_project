import axios from "axios";

export default {
    actions: {
        async fetchTopics(ctx, search) {
            let res
            if (search === undefined)
                res = await axios.get('api/topics/')
            else
                res = await axios.get(`api/topics/?search=${search}`)

            ctx.commit('updateTopics', res.data)
        }
    },
    mutations: {
        updateTopics(state, topics) {
            state.topics = topics
        }
    },
    getters: {
        getTopics(state) {
            return state.topics
        }
    },
    state: {
        topics: []
    }
}