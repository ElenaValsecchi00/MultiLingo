import { createI18n } from "vue-i18n";
export default createI18n({
  locale: import.meta.env.VITE_DEFAULT_LOCALE, // <--- 1
  fallbackLocale: import.meta.env.VITE_FALLBACK_LOCALE, // <--- 2
  globalInjection: true,
  legacy: false, // <--- 3
  messages: {
    en: {
      nav: {
        home: "Home",
        about: "About"
      },
      home: {
        header: "Welcome!",
        choose_flag: "Choose the language you prefer"
      },
      about: {
        header: "About us"
      }
    },
    it: {
        nav: {
          home: "Home",
          about: "About"
        },
        home: {
          header: "Benvenuti!",
          choose_flag: "Scegli la lingua che preferisci"
        },
        about: {
          header: "Su di noi(L'amore è una favola)"
        }
      }
    }
})

