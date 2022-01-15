import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login/Login.vue'
import Register from '../views/Login/Register.vue'
import EmailVerify from '../views/Login/EmailVerify.vue'
import NewPassword from '../views/Login/NewPassword.vue'
import ResetPassword from '../views/Login/ResetPassword.vue'
import MySchool from '../views/MySchool.vue'
import Step0 from '../views/Add/Step0.vue'
import Step1 from '../views/Add/Step1.vue'
import Step2 from '../views/Add/Step2.vue'
import Step3 from '../views/Add/Step3.vue'
import Step4 from '../views/Add/Step4.vue'
import Error from '../views/Error.vue'
import Poll from '../views/Poll.vue'
import EditSubject from '../views/Edit/EditSubject.vue'
import EditTeacher from '../views/Edit/EditTeacher.vue'
import EditClassroom from '../views/Edit/EditClassroom.vue'
import EditClass from '../views/Edit/EditClass.vue'
import Wait from '../views/Add/Spinner.vue'

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
    path: '/edit/Subject/:id',
    name: 'EditSubject',
    component: EditSubject
  },
  {
    path: '/edit/teacher',
    name: 'EditTeacher',
    component: EditTeacher
  },
  {
    path: '/edit/classroom',
    name: 'EditClassroom',
    component: EditClassroom
  },
  {
    path: '/edit/class',
    name: 'EditClass',
    component: EditClass
  },
  {
    path: '/wait',
    name: 'Wait',
    component: Wait
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
