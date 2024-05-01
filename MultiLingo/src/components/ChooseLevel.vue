<template>
    <img :src="get_flag()" alt="flag">
    <header>
        <p>{{ $t("language.header") }}</p>
    </header>
    <RouterView />
</template>

<script setup>
import router from '../router';
import { useRoute } from 'vue-router';
function get_flag(){return(useRoute().params.flag);}
</script>

<style>
img{
    display: inline-block;
    width:10%;
    align-self: right;
}
</style>