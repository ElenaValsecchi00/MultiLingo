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
        choose_flag: "Choose the language you prefer and start navigating through the app using the words 'Confirm' and 'Back' ",
        choose_starting_flag: "Choose your first language"
      },
      language: {
        header: "Choose the level",
        level: "Lev."
      },
      assignment:{
        header_1_1: "Choose the correct word and pronounce it",
        header_1_2: "Listen and complete the sentence",
        header_1_3: "Listen and reorder the sentence",
        header_result_1: "Results Level 1",
        header_2_1: "Translate the phrase and then read it",
        header_2_2: "Listen the phrase and then translate it",
        header_result_2:"Results Level 2" ,
        header_3: "Welcome to Megastore! Are you looking for fruit, tools or clothes?",
        header_03: "Write or pronounce your answers",
        confirm: "Confirm"
      }
    },
    it: {
      home: {
        header: "Benvenuto/a!",
        choose_flag: "Scegli la lingua che preferisci e inizia a navigare nell'applicazione utilizzando le parole 'Conferma' e 'Indietro' ",
        choose_starting_flag: "Scegli la lingua di partenza"
      },
        language: {
          header: "Scegli il livello",
          level: "Liv."
        },
        assignment:{
          header_1_1: "Scegli l'opzione corretta e pronunciala",
          header_1_2: "Ascolta e completa la frase",
          header_1_3: "Ascolta la frase e riordinala",
          header_result_1: "Risultati Livello 1",
          header_2_1: "Traduci la frase e leggila",
          header_2_2: "Ascolta la frase e traducila",
          header_result_2:"Risultati Livello 2" ,
          header_03: "Scrivi o pronuncia le tue risposte",
          header_3: "Benvenuto in Megastore! Stai cercando frutta, attrezzi o vestiti?",
          confirm: "Conferma"
        }
      },
    es: {
      home: {
        header: "Bienvenido!",
        choose_flag: "Selecciona el idioma que prefieres y empieza a navegar por la aplicación con las palabras 'Confirma' y 'Atràs' ",
        choose_starting_flag: "Selecciona tu primer idioma"
      },
        language: {
          header: "Selecciona el nivel",
          level: "Niv."
        },
        assignment:{
          header_1_1: "Selecciona la correcta opcion y léela",
          header_1_2: "Escucha y completa la frase",
          header_1_3: "Escusa la frase y ordenala",
          header_result_1: "Resultados Nivel 1",
          header_2_1: "Traduce la frase y léela",
          header_2_2: "Escucha la frase y traduzla",
          header_result_2:"Resultados Nivel 2" ,
          header_03: "Escribir o pronunciar las respuestas",
          header_3: "¡Bienvenidos a Megatienda! ¿Buscas fruta, herramientas o ropa?",
          confirm: "Confirma"
        }
    },
    fr: {
      home: {
        header: "Bienvenue!",
        choose_flag: "Choisissez la langue que vous préférez et commencez à naviguer dans l'application avec les mots 'Confirme' et 'Arrière' ",
        choose_starting_flag: "Choisissez votre langue maternelle"
      },
        language: {
          header: "Choisissez le niveau",
          level: "Niv."
        },
        assignment:{
          header_1_1: "Choisissez l'option correcte et lisez-la",
          header_1_2: "Écoutez et complétez la phrase",
          header_1_3: "Écoutez et ordonnez la phrase",
          header_result_1: "Résultats Niveau 1",
          header_2_1: "Traduis la phrase et lis-la",
          header_2_2: "Écoute la phrase et traduis-la",
          header_result_1: "Résultats Niveau 2",
          header_03: "Écrivir ou prononcer les responses",
          header_3: "Bienvenue sur Mégastore! Vous cherchez des fruits, des outils ou des vêtements?",
          confirm: "Confirme"
        }
      }
}
})

