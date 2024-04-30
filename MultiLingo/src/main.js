import './assets/main.css'

import { createApp } from 'vue/dist/vue.esm-bundler'
import { createPinia } from 'pinia'
import i18n from "./i18n" 

import App from './App.vue'
import router from './router'
import CountryFlag from 'vue-country-flag-next'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)
app.use(CountryFlag)

app.mount('#app')

