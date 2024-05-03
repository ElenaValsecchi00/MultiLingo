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
      },
      assignment:{
        header: "Complete the sentence",
        phrase: "The cat is ... the table",
        answers: ["on", "under"],
        confirm: "Confirm"
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
        },
        assignment:{
          header: "Completa la frase",
          phrase: "Il gatto è ... tavolo",
          answers: ["sul", "sotto al"],
          confirm: "Conferma"
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
        },
        assignment:{
          header: "Completa la frase",
          phrase: "Il gatto è ... tavolo",
          answers: ["sul", "sotto al"],
          confirm: "Bestätigt"
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
        },
        assignment:{
          header: "Complétez cette phrase",
          phrase: "Le chat est ... la table",
          answers: ["sur", "sous"],
          confirm: "Confirme"
        }
      }
}
})

