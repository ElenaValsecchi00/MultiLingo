<script setup>
import router from '../router'
import { useRoute } from 'vue-router';

//pass right language to levels
function goToLanguage(route, flag){
    router.push({name:route, params:{flag}})
}

//return right flag
function it_flag (){ return("https://cdn.countryflags.com/thumbs/italy/flag-square-250.png");}
function fr_flag (){ return("https://cdn.countryflags.com/thumbs/france/flag-square-250.png");}
function ge_flag (){ return("https://cdn.countryflags.com/thumbs/germany/flag-square-250.png");}
function uk_flag (){ return("https://cdn.countryflags.com/thumbs/united-kingdom/flag-square-250.png");}


</script>

<template>
  <header>
    <p>{{ $t("home.header") }}</p>
  </header>
  <div id="flags">
    <button @click="goToLanguage('levels',it_flag())"><img :src="it_flag()" alt="italian"></button>
    <button @click="goToLanguage('levels', fr_flag())"><img :src="fr_flag()" alt="french"></button>
    <button @click="goToLanguage('levels',ge_flag())"><img :src="ge_flag()" alt="brithish"></button>
    <button @click="goToLanguage('levels', uk_flag())"><img :src="uk_flag()" alt="german"></button>
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
/*
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
*/
</style>
