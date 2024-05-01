import { createI18n } from "vue-i18n";
export default createI18n({
  locale: import.meta.env.VITE_DEFAULT_LOCALE, // <--- 1
  fallbackLocale: import.meta.env.VITE_FALLBACK_LOCALE, // <--- 2
  globalInjection: true,
  legacy: false, // <--- 3
  messages: {
    en: {
      home: {
        header: "Welcome!",
        choose_flag: "Choose the language you prefer"
      },
      language: {
        header: "Choose the level"
      }
    },
    it: {
        nav: {
          home: "Home",
          about: "About"
        },
        language: {
          header: "Scegli il livello"
        }
      }
    }
})

