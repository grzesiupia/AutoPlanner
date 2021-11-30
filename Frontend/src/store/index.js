import Vue from 'vue'
import Vuex from 'vuex'


import login from './modules/login'
import register from './modules/register'
import subjects from './modules/subjects'
import teachers from './modules/teachers'
import classrooms from './modules/classrooms'
import classes from './modules/classes'
import * as actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  actions,
  modules: {
    login,
    register,
    subjects,
    teachers,
    classrooms,
    classes
  }
})
