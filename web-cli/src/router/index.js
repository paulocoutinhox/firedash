import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/pages/Home'
import Dashboards from '@/components/pages/Dashboards'
import Login from '@/components/pages/Login'
import ControlPanelHome from '@/components/pages/control-panel/ControlPanelHome'

import DeviceHome from '@/components/pages/control-panel/device/DeviceHome'
import DeviceCreate from '@/components/pages/control-panel/device/DeviceCreate'
import DeviceUpdate from '@/components/pages/control-panel/device/DeviceUpdate'
import DeviceView from '@/components/pages/control-panel/device/DeviceView'

import AccountHome from '@/components/pages/control-panel/account/AccountHome'
import AccountCreate from '@/components/pages/control-panel/account/AccountCreate'
import AccountUpdate from '@/components/pages/control-panel/account/AccountUpdate'
import AccountView from '@/components/pages/control-panel/account/AccountView'

import ProfileUpdate from '@/components/pages/control-panel/profile/ProfileUpdate'
import ProfileUpdatePassword from '@/components/pages/control-panel/profile/ProfileUpdatePassword'

import store from '@/store.js'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/dashboards',
      name: 'Dashboards',
      component: Dashboards,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/control-panel',
      name: 'ControlPanelHome',
      component: ControlPanelHome,
      meta: {
        requiresAuth: true,
        requiresAuthAsAdmin: true
      }
    },
    {
      path: '/control-panel/device',
      name: 'DeviceHome',
      component: DeviceHome,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/device/create',
      name: 'DeviceCreate',
      component: DeviceCreate,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/device/update/:id',
      name: 'DeviceUpdate',
      component: DeviceUpdate,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/device/view/:id',
      name: 'DeviceView',
      component: DeviceView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/account',
      name: 'AccountHome',
      component: AccountHome,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/account/create',
      name: 'AccountCreate',
      component: AccountCreate,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/account/update/:id',
      name: 'AccountUpdate',
      component: AccountUpdate,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/account/view/:id',
      name: 'AccountView',
      component: AccountView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/profile/update',
      name: 'ProfileUpdate',
      component: ProfileUpdate,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/control-panel/profile/update-password',
      name: 'ProfileUpdatePassword',
      component: ProfileUpdatePassword,
      meta: {
        requiresAuth: true
      }
    },
    { path: '*', redirect: '/' }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (to.matched.some(record => record.meta.requiresAuthAsAdmin)) {
      if (store.getters.isCurrentAccountAdmin) {
        next()
      } else {
        next({
          path: '/login',
          params: { nextUrl: to.fullPath }
        })
      }
    } else {
      if (store.getters.isLoggedIn) {
        next()
      } else {
        next({
          path: '/login',
          params: { nextUrl: to.fullPath }
        })
      }
    }
  } else {
    next()
  }
})

export default router