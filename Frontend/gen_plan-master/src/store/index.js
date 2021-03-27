import Vue from 'vue'
import Vuex from 'vuex'


import login from './modules/login'
import register from './modules/register'
import * as actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  actions,
  modules: {
    login,
    register,
  }
})
