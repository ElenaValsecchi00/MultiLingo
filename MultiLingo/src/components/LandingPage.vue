<script>
import i18n from '@/i18n';
import router from '../router'

//pass right language to levels
function goToLanguage(route,language){
  i18n.global.locale.value=language;
  router.push({name:route, params:{language}})
}
export default {
    data() {
    },
    created(){
    },
    methods: {
        goToLanguage(route,language){
            i18n.global.locale.value=language;
        router.push({name:route, params:{language}})
      }
    }
    };
</script>

<template>
  <header>
    <p>{{ $t("home.header") }}</p>
  </header>
  <div id="flags">
    <button @click="goToLanguage('levels','it')"><img src="../../flags/it.png" alt="italian"></button>
    <button @click="goToLanguage('levels','fr')"><img src="../../flags/fr.png" alt="french"></button>
    <button @click="goToLanguage('levels','ge')"><img src="../../flags/ge.png" alt="german"></button>
    <button @click="goToLanguage('levels','en')"><img src="../../flags/en.png" alt="british"></button>
  </div>
  <p>{{ $t("home.choose_flag") }}</p>
  <RouterView />
</template>

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
