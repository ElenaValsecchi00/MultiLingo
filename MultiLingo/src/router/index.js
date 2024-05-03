import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../components/LandingPage.vue'
import ChooseLevelPage from '../components/ChooseLevel.vue'
import Ex1Page from '../components/Ex1.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingPage
    },
    {
      path: '/levels/:language',
      name: 'levels',
      component: ChooseLevelPage
    },
    {
      path: '/:language/ex1',
      name: 'ex1',
      component: Ex1Page
    }
  ]
})

export default router
