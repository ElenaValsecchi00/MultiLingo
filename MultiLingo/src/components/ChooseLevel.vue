<template>
    <header>
        <div class="container">
            <button @click="goBack()" class="back_button">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
            </svg>
            </button>
            <img :src="src" alt="flag">
            <div><p id="title">{{ $t("language.header") }}</p></div>
        </div>
    </header>
    <div id="levels">
        <div class="ellipse" @click="goEx(1)">
            <p>{{ $t("language.level") }}1</p>
        </div>
        
        <div class="ellipse" @click="goEx(2)">
            <p>{{ $t("language.level") }}2</p>
        </div>
        
        <div class="ellipse" @click="goEx(3)">
            <p>{{ $t("language.level") }}3</p>
        </div>

    </div>
    
    <RouterView />
</template>

<script>
import router from '../router';
import { useRoute } from 'vue-router';
import axios from 'axios';

export default{
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
    goBack(){
        router.go(-1);
    },
    goEx(i){
        if(i === 2){
            router.push({name:"lev" + i + "choice"});
        }else{
            router.push({name:"lev" + i});
        }
        
    }
    
}
};

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