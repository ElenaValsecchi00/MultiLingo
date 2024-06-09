<template>
    <body>
        <header>
            <div class="container">
                <button @click="goBack()" class="back_button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                </svg>
                </button>
                <img :src='src' class="flag" alt="flag">
            </div>
        </header>
        <div>
            <p>{{ $t("assignment.header_result_2") }}</p>
            <p>E-1: {{ this.result2_1}} /1</p>
            <p>E-2: {{ this.result2_2}} /1</p>
        </div>
        <button class="buttonConferma" @click="goOn()">{{ $t("assignment.confirm") }}</button>
    
    </body>
</template>
  
<script>
import router from '@/router';
import axios from "axios"
export default {
    data() {
        return {
            flag: null,
            result2_1: '',
            result2_2: '',
        };
    },

    created(){
        this.flag = this.$route.params.language;
        this.src = '../../flags/' + this.flag + ".png";
        
        this.getResults()
    },
    mounted() {
        
    },
    methods: {  
        goBack(){
        router.go(-1);
        },
        getResults(){
            axios.get('http://127.0.0.1:5000/lev1/results', {ex: "2"})
        .then(response => {
            console.log(response.data)
            this.result2_1 = response.data["1"]
            this.result2_2 = response.data["2"]
        })
        },
        goOn(){
            router.go(-1);
        }
    }
    };
</script>

<style scoped>
body{
    background-color: #FBF2D4;
    
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
.container{
    position:relative;
    margin:0cap;
}

.flag{
    position:absolute;
    display: inline;
    width:10%;
    right:0;
    margin-top: 1cap;
    margin-right: 1cap;
}
</style>
