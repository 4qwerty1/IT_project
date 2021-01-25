import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// import modules
import messages from "@/store/messages";
import topics from "@/store/topics";

export default new Vuex.Store({
    modules: {
        messages,
        topics,
    }
})
