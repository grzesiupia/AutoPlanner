import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import EmailVerify from '../views/EmailVerify.vue'
import NewPassword from '../views/NewPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'
import MySchool from '../views/MySchool.vue'
import Step0 from '../views/Step0.vue'
import Step1 from '../views/Step1.vue'
import Step2 from '../views/Step2.vue'
import Step3 from '../views/Step3.vue'
import Step4 from '../views/Step4.vue'
import Error from '../views/Error.vue'
import Poll from '../views/Poll.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/register/verify',
    name: 'EmailVerify',
    component: EmailVerify
  },
  {
    path: '/reset/password',
    name: 'ResetPassword',
    component: ResetPassword
  },
  {
    path: '/new/password',
    name: 'NewPassword',
    component: NewPassword
  },
  {
    path: '/my/school',
    name: 'MySchool',
    component: MySchool
  },
  {
    path: '/step/0',
    name: 'Step0',
    component: Step0
  },
  {
    path: '/step/1',
    name: 'Step1',
    component: Step1
  },
  {
    path: '/step/2',
    name: 'Step2',
    component: Step2
  },
  {
    path: '/step/3',
    name: 'Step3',
    component: Step3
  },
  {
    path: '/step/4',
    name: 'Step4',
    component: Step4
  },
  {
    path: '/poll/:id',
    name: 'Poll',
    component: Poll
  },
  {
    path: "*",
    component: Error
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
