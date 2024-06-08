<template>
  <header>
    <p>{{ $t("home.header") }}</p>
  </header>
  <div id="flags">
    <button @click="goToLanguage('levels','it')"><img src="../../flags/it.png" alt="italian"></button>
    <button @click="goToLanguage('levels','fr')"><img src="../../flags/fr.png" alt="french"></button>
    <button @click="goToLanguage('levels','es')"><img src="../../flags/es.png" alt="spanish"></button>
    <button @click="goToLanguage('levels','en')"><img src="../../flags/en.png" alt="british"></button>
  </div>
  <p>{{ $t("home.choose_flag") }}</p>
  <RouterView />
</template>

<script>
import i18n from '@/i18n';
import router from '../router';
import axios from 'axios';

export default {
  
    methods: {
        goToLanguage(route,language){
          i18n.global.locale.value=language;
          this.sendLanguage(language);
          this.listen_in_back();
          router.push({name:route, params:{language}})
      },
      sendLanguage(language) {    
        axios.post('http://127.0.0.1:5000/', {language:language})
        .then(response => { 
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        });
        },
        listen_in_back(){
        axios.post('http://127.0.0.1:5000/background')
        .then(response => { 
          console.log(response.data["url"]);
          router.replace({name:response.data["url"]});
        })
        .catch(error => {
            console.log(error)
        });
    }
    }
    };
</script>

<style scoped>

button{
    background-color: transparent;
    background-repeat: no-repeat;
    border: none;
    cursor: pointer;
    overflow: hidden;
    outline: none;
}

header{
    margin-top: 3em;
}

img{
  width: 100%;
}

#flags{
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

</style>
