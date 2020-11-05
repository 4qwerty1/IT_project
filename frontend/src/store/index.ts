import {createStore} from 'vuex'

export default createStore({
    state: {
        regForm: {
            name: '',
            surname: '',
            sex: null,
            language: 'Любимый ЯП',
            pattern: 'Любимый pattern'
        }
    },
    getters: {
        getForm: state => {
            return state.regForm
        },
        getFormName: state => {
            return state.regForm.name
        }
    },
    mutations: {},
    actions: {},
    modules: {}
})
