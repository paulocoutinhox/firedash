import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

let store = new Vuex.Store({
    state: {
        authStatus: '',
        token: localStorage.getItem('token') || '',
        account: (localStorage.getItem('account') ? JSON.parse(localStorage.getItem('account')) : {})
    },
    mutations: {
        authRequest(state) {
            state.authStatus = 'loading'
        },
        authSuccess(state, payload) {
            state.authStatus = 'success'
            state.token = payload.token
            state.account = payload.account
        },
        profileUpdated(state, payload) {
            state.account = payload.account
            localStorage.setItem('account', JSON.stringify(payload.account))
        },
        authError(state) {
            state.authStatus = 'error'
        },
        logout(state) {
            state.authStatus = ''
            state.token = ''
            state.account = ''
        }
    },
    actions: {
        login({ commit }, account) {
            return new Promise((resolve, reject) => {
                commit('authRequest')
                axios({ url: '/api/auth/login', data: account, method: 'POST' })
                    .then(resp => {
                        if (resp.data.success) {
                            const token = resp.data.data.token
                            const account = resp.data.data.account

                            localStorage.setItem('token', token)
                            localStorage.setItem('account', JSON.stringify(account))

                            delete axios.defaults.headers.common['Authorization']
                            axios.defaults.headers.common['Authorization'] = 'Bearer: ' + token

                            commit('authSuccess', { 'token': token, 'account': account })
                            resolve(resp.data)
                        } else {
                            commit('authError')
                            localStorage.removeItem('token')
                            localStorage.removeItem('account')
                            reject(resp.data)
                        }
                    })
                    .catch(err => {
                        commit('authError')
                        localStorage.removeItem('token')
                        localStorage.removeItem('account')
                        reject()
                    })
            })
        },
        logout({ commit }) {
            return new Promise((resolve, reject) => {
                commit('logout')

                localStorage.removeItem('token')
                localStorage.removeItem('account')

                delete axios.defaults.headers.common['Authorization']

                resolve()
            })
        }
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.authStatus,
        currentAccount: state => state.account,
        currentToken: state => state.token,
        isCurrentAccountAdmin: state => (state.account != null && state.account.is_admin == true),
    }
})

if (store.getters.currentToken) {
    delete axios.defaults.headers.common['Authorization']
    axios.defaults.headers.common['Authorization'] = 'Bearer: ' + store.getters.currentToken
}

export default store