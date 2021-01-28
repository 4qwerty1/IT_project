import axios from "axios";

export default {
    actions: {
        async fetchMessages(ctx, topicId) {
            const res = await axios.get(`api/messages/?topic=${topicId}`)
            ctx.commit('updateMessages', res.data)
        },
        async fetchNewMessages(ctx, topicId) {
            const time = ctx.getters.getLastMsgTime
            let res
            if (time !== undefined)
                res = await axios.get(`api/messages/?topic=${topicId}&last_message=${time}`)
            else
                res = await axios.get(`api/messages/?topic=${topicId}`)

            ctx.commit('addMessages', res.data)
        }
    },
    mutations: {
        updateMessages(state, messages) {
            state.messages = messages
        },
        addMessages(state, messages) {
            state.messages.push(...messages)
        }
    },
    getters: {
        getMessages(state) {
            return state.messages
        },
        getLastMsgTime(state) {
            if (state.messages.length === 0) return undefined
            return state.messages[state.messages.length - 1]
                .time_create
        }
    },
    state: {
        messages: []
    }
}