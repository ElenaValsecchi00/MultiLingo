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
        choose_flag: "Choose the language you prefer",
        choose_starting_flag: "Choose your first language"
      },
      language: {
        header: "Choose the level",
        level: "Lev."
      },
      assignment:{
        header_1_1: "Complete the sentence",
        header_1_2: "Listen and complete the sentence",
        header_1_3: "Order the sentence",
        header_2_1: "Translate the phrase and then read it",
        header_2_2: "Listen the phrase and then translate it",
        header_3: "Welcome to Megastore! Are you looking for fruit, tools or clothes?",
        confirm: "Confirm"
      }
    },
    it: {
      home: {
        header: "Benvenuto/a!",
        choose_flag: "Scegli la lingua che preferisci",
        choose_starting_flag: "Scegli la lingua di partenza"
      },
        language: {
          header: "Scegli il livello",
          level: "Liv."
        },
        assignment:{
          header_1_1: "Completa la frase",
          header_1_2: "Ascolta e completa la frase",
          header_1_3: "Riordina la frase",
          header_2_1: "Traduci la frase e leggila",
          header_2_2: "Ascolta la frase e traducila",
          header_3: "Benvenuto in Megastore! Stai cercando frutta, attrezzi o vestiti?",
          confirm: "Conferma"
        }
      },
    es: {
      home: {
        header: "Bienvenido!",
        choose_flag: "Selecciona el idioma que prefieres",
        choose_starting_flag: "Selecciona tu primer idioma"
      },
        language: {
          header: "Selecciona el nivel",
          level: "Niv."
        },
        assignment:{
          header_1_1: "Completa la frase",
          header_1_2: "Escucha y completa la frase",
          header_1_3: "Ordena la frase",
          header_2_1: "Traduce la frase y léela",
          header_2_2: "Escucha la frase y traduzla",
          header_3: "¡Bienvenidos a Megatienda! ¿Buscas fruta, herramientas o ropa?",
          confirm: "Confirma"
        }
    },
    fr: {
      home: {
        header: "Bienvenue!",
        choose_flag: "Choisissez la langue que vous préférez",
        choose_starting_flag: "Choisissez votre langue maternelle"
      },
        language: {
          header: "Choisissez le niveau",
          level: "Niv."
        },
        assignment:{
          header_1_1: "Complétez cette phrase",
          header_1_2: "Écoutez et complétez la phrase",
          header_1_3: "Ordonnez la phrase",
          header_2_1: "Traduis la phrase et lis-la",
          header_2_2: "Écoute la phrase et complète-la",
          header_3: "Bienvenue sur Mégastore! Vous cherchez des fruits, des outils ou des vêtements?",
          confirm: "Confirme"
        }
      }
}
})

