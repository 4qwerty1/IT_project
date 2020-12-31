import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// import modules
import topicMessages from './topicMessages'
import topicList from './topicList'

export default new Vuex.Store({
    modules: {
        topicMessages,
        topicList,
    }
})
