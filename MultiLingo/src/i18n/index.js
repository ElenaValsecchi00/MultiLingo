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
        header: "Welcome to the Vue 3 I18n tutorial!",
        created_by: "This tutorial was brought to you by Lokalise."
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
          header: "benvenuti nel tutorial di Vue 3 I18n!",
          created_by: "Il tutorial è offerto da Elena."
        },
        about: {
          header: "Su di noi(L'amore è una favola)"
        }
      }
    }
})

const messages = {
    en: {
      nav: {
        home: "Home",
        about: "About"
      },
      home: {
        header: "Welcome to the Vue 3 I18n tutorial!",
        created_by: "This tutorial was brought to you by Lokalise."
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
          header: "benvenuti nel tutprial di Vue 3 I18n!",
          created_by: "Il tutorial è offerto da Lokalize."
        },
        about: {
          header: "Su di noi"
        }
      }
  }