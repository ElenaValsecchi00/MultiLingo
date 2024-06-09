<template>
  <body>
    <header>
        <div class="container">
            <button @click="goBack()" class="back_button">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
            </svg>
            </button>
            <img class="imgHeader" :src="src" alt="flag">
            <div><p id="title">{{ $t("home.choose_starting_flag") }}</p></div>
        </div>
    </header>
    <!--
    <div id="flags">
      <button @click="sendLanguage('it')"><img class ="flagImg" src="../../flags/it.png" alt="italian"></button>
      <button @click="sendLanguage('fr')"><img class ="flagImg" src="../../flags/fr.png" alt="french"></button>
      <button @click="sendLanguage('es')"><img class ="flagImg" src="../../flags/es.png" alt="spanish"></button>
      <button @click="sendLanguage('en')"><img class ="flagImg" src="../../flags/en.png" alt="british"></button>
    </div>
    -->
    <form>
      <input class="languageinput" v-model="language" placeholder="what is your native language? ex:it,es,en,fr"/>
      <a href="#" v-on:click="sendLanguage(language)" id="submit">SUBMIT</a>
    </form>
    <RouterView />

    <button class="buttonConferma" @click="goOn()">{{ $t("assignment.confirm") }}</button>
  </body>

  </template>
  
  <script>
  import i18n from '@/i18n';
  import router from '../router';
  import axios from 'axios';
  
  export default {
    data() {
        return {
        flag: null,
        src: ""
        };
    },
    created() {
        // Accesso al parametro della route
        this.flag = this.$route.params.language;
        // Composizione della stringa utilizzando il parametro della route
        this.src = '../../flags/' + this.flag + ".png";
    },
      methods: {
        sendLanguage(language) {    
          axios.post('http://127.0.0.1:5000/lev2/getLanguage', {startingLanguage:language})
          .then(response => { 
              console.log(response)
              //router.replace({name:"lev2", params: this.flag})
          })
          .catch(error => {
              console.log(error)
          });
          },
        goBack(){
            router.go(-1);
        },
        goOn(){
          setTimeout(function(){router.replace({name:"lev2", params: this.flag})}, 1000)
        }
      }
      };
  </script>
  
<style scoped>

body{
    background-color: #FBF2D4;
}

#submit{
  position: relative;
  top: 250px;
  right: 150px;
}

#flags{
  margin-top:10rem;
  display: grid;
  grid-auto-flow: row;
  grid-gap: 10px;
  row-gap: 20px;
  column-gap: 20px;
  grid-template-rows: auto auto;
  grid-template-columns: auto auto;
  justify-content: center;
  padding: 40px;
}

.imgHeader{
    position:absolute;
    display: inline;
    width:10%;
    right:0;
    margin-top: 1cap;
    margin-right: 1cap;
}
button{
    background-color: transparent;
    background-repeat: no-repeat;
    border: none;
    cursor: pointer;
    overflow: hidden;
    outline: none;
}

.buttonConferma {
    position:absolute;
    width: 50%;
    height: 40px;
    text-align: center;
    left: 0; 
    right: 0; 
    bottom:40px;
    margin-left: auto; 
    margin-right: auto; 
    background: #C3E986;
    border-radius: 10px;
    border-color: transparent;
    cursor: pointer;
}
.languageinput{
  border-radius: 10px;
  position: relative;
  top:200px;
  left:30px;
  width:300px;
  height:50px;
  text-align: center;
}

img{
  width: 100%;
}
.back_button{
    background-color: transparent;
    background-repeat: no-repeat;
    border: none;
    cursor: pointer;
    overflow: hidden;
    outline: none;
    margin-top: 1cap;
    margin-left: 1cap;
}

#title{
    margin-top: 3cap;
    position: absolute;
    display: inline;
    width: 100%;
    right:width/2;
}

  </style>
  