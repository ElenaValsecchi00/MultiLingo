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
import { useRoute } from 'vue-router';

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
            try{
              if (response.data["url"]=="back")
              {
                console.log("back");
                router.go(-1);
              }
              else if(response.data["url"]=="confirm"){
                var routName =router.currentRoute.value.name
                for(let i=0; i<router.getRoutes().length; i++)
                {
                  var r = router.getRoutes()[i];
                  if(r.name==routName){
                    var goOn = r.components.default.methods.goOn;
                    goOn();
                  }
                
                }
              }
              else if (response.data["url"]=="level one")
              {
                this.findRoute(1)
              }
              else if (response.data["url"]=="level two")
              {
                this.findRoute(2)
              }
              else if (response.data["url"]=="level three")
              {
                this.findRoute(3)
              }
              this.listen_in_back()
          }
          catch(error){
            console.log(error)
            this.listen_in_back()
          }
        })
        .catch(error => {
            console.log(error)
        });
    },
    findRoute(trigger){
      var routName =router.currentRoute.value.name
      console.log(routName, router.getRoutes())
        for(let i=0; i<router.getRoutes().length; i++)
        {
          var r = router.getRoutes()[i];
          if(r.name==routName){
            console.log(r.components.default.methods)
            var goEx = r.components.default.methods.goEx;
            goEx(trigger);
          }
        }
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
