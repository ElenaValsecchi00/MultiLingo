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
        header_1_1: "Complete the sentence",
        header_1_2: "Listen and complete the sentence",
        header_1_3: "Answer the questions",
        header_3: "Welcome to Megastore! Are you looking for food, tools or clothes?",
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
          header_1_1: "Completa la frase",
          header_1_2: "Ascolta e completa la frase",
          header_1_3: "Rispondi alle domande",
          header_3: "Benvenuto in Megastore! Stai cercando frutta, attrezzi o vestiti?",
          confirm: "Conferma"
        }
      },
    es: {
      home: {
        header: "Bienvenido!",
        choose_flag: "Selecciona el idioma que prefieres"
      },
        language: {
          header: "Selecciona el nivel",
          level: "Niv."
        },
        assignment:{
          header_1_1: "Completa la frase",
          header_1_2: "Escucha y completa la frase",
          header_1_3: "Responde a las preguntas",
          header_3: "Benvenuto in Megastore! Stai cercando frutta, attrezzi o vestiti?",
          confirm: "Confirma"
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
          header_1_1: "Complétez cette phrase",
          header_1_2: "Écoutez et complétez la phrase",
          header_1_3: "Répondez aux questions",
          header_3: "Benvenuto in Megastore! Stai cercando frutta, attrezzi o vestiti?",
          confirm: "Confirme"
        }
      }
}
})

