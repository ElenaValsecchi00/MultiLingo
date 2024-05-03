<template>
    <header>
        <div class="container">
            <button @click="goBack()" class="back_button">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
            </svg>
            </button>
            <img :src="get_flag()" alt="flag">
            <div><p id="title">{{ $t("language.header") }}</p></div>
        </div>
    </header>
    <div id="levels">
        <div class="ellipse">
            <p>{{ $t("language.level") }}1</p>
        </div>
        
        <div class="ellipse">
            <p>{{ $t("language.level") }}2</p>
        </div>
        
        <div class="ellipse">
            <p>{{ $t("language.level") }}3</p>
        </div>

        <button @click="fetchData()"><p>{{message}}</p></button>
    </div>
    <div>

    </div>
    <RouterView />
</template>

<script setup>
import router from '../router';
import { useRoute } from 'vue-router';
import axios from 'axios';


function get_flag(){return(useRoute().params.flag);} //returns the right flag
function goBack(){router.push({name:'home'});}

let message="";

//Va messo nella pagina dei singoli livelli
function fetchData() {
      axios.get('http://localhost:5000')
        .then(response => {
          console.log(response.data);
          // do something with response.data
        })
        .catch(error => {
          console.error(error);
        });
}

</script>

<style scoped>
img{
    position:absolute;
    display: inline;
    width:10%;
    right:0;
    margin-top: 1cap;
    margin-right: 1cap;
}

.container{
    position:relative;
    margin:0cap;
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

.ellipse{
    width: 88px;
    height: 82px;
    border-radius: 50%;
    margin-bottom: 3cap;
    margin-left:40%;
    background: #C3E986;
}

.ellipse:nth-child(2){
    background: #F3C581;
}

.ellipse:nth-child(3){
    background: #E27676;
}

#title{
    margin-top: 3cap;
    position: absolute;
    display: inline;
    width: 100%;
    right:width/2;
}

#levels{
    margin-top:20cap;
}
</style>