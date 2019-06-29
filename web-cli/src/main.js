// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'es6-promise/auto'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.use(Buefy)

import axios from 'axios'
Vue.prototype.$http = axios

import store from '@/store.js'
import App from '@/App'
import router from '@/router'

import VueTimers from 'vue-timers'
Vue.use(VueTimers)

import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)

import VueClipboard from 'vue-clipboard2'
Vue.use(VueClipboard)

Vue.use(require('vue-moment'))

import '@mdi/font/css/materialdesignicons.css'
import '@/assets/css/main.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
