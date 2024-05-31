import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../components/LandingPage.vue'
import ChooseLevelPage from '../components/ChooseLevel.vue'
import Lev1Page from '../components/Lev1.vue'
import Lev2Page from '../components/Lev2.vue'
import Lev2_2Page from '../components/Lev2_2.vue'
import Lev1_2Page from '../components/Lev1_2.vue'
import Lev1_3Page from '../components/Lev1_3.vue'
import Lev3Page from '../components/Lev3.vue'
import Lev2Choice from '../components/Lev2Choice.vue'

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
      path: '/:language/lev1',
      name: 'lev1',
      component: Lev1Page
    },
    {
      path: '/:language/lev2',
      name: 'lev2',
      component: Lev2Page
    },
    {
      path: '/:language/lev2_2',
      name: 'lev2_2',
      component: Lev2_2Page
    },
    {
      path: '/:language/lev3',
      name: 'lev3',
      component: Lev3Page
    },
    {
      path: '/:language/lev1_2',
      name: 'lev1_2',
      component: Lev1_2Page
    },
    {
      path: '/:language/lev1_3',
      name: 'lev1_3',
      component: Lev1_3Page
    },
    {
      path: '/:language/lev2choice',
      name: 'lev2choice',
      component: Lev2Choice
    }
  ]
})

export default router
