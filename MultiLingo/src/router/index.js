import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../components/LandingPage.vue'
import ChooseLevelPage from '../components/ChooseLevel.vue'
import Ex1Page from '../components/Ex1.vue'
import Ex2Page from '../components/Ex2.vue'
import Ex3Page from '../components/Ex3.vue'
import Ex1Page1 from '../components/Ex1_1.vue'
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
    },
    {
      path: '/:language/ex1/1',
      name: 'ex1/1',
      component: Ex1Page1
    },
    {
      path: '/:language/ex2',
      name: 'ex2',
      component: Ex2Page
    },
    {
      path: '/:language/ex3',
      name: 'ex3',
      component: Ex3Page
    }
  ]
})

export default router
