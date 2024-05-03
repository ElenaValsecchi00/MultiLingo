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
        header: "Choose the level",
        level: "Lev."
      }
    },
    it: {
      home: {
        header: "Benvenuto/a!",
        choose_flag: "Scegli la lingua che preferisci"
      },
        language: {
          header: "Scegli il livello",
          level: "Liv."
        }
      },
    ge: {
      home: {
        header: "Wilkommen!",
        choose_flag: "Wählen Sie Ihre bevorzugte Sprache"
      },
        language: {
          header: "Wählen Sie die Dringlichkeitsstufe",
          level: "Eb."
        }
    },
    fr: {
      home: {
        header: "Bienvenue!",
        choose_flag: "Choisissez la langue que vous préférez"
      },
        language: {
          header: "Choisissez le niveau",
          level: "Niv."
        }
      }
}
})

