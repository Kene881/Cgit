import { createRouter, createWebHistory } from 'vue-router'
import Projects from '../views/Projects.vue'
import Login from '../views/Login.vue'
import Comments from '../views/Comments'

const routes = [
  {
    path: '',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path:'/comments/:id_pr',
    name:'comments',
    component: Comments
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
