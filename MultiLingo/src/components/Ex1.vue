<template>
    <body>
        <header>
            <div class="container">
                <button @click="goBack()" class="back_button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                </svg>
                </button>
                <img :src="src" alt="flag">
            </div>
            
        </header>
        <div>
            <p>{{ $t("assignment.header") }}</p>
            <p>{{ this.phrase }}</p>
        </div>
        <div>
            <!--Fare il for sugli elementi-->
            <p class="clickable-div" :class="{ 'clickable': selectedParagraph === 0 }"
            @click="selectParagraph(0)">
                {{ $t("assignment.answers.0") }}
            </p>
            <p class="clickable-div" :class="{ 'clickable': selectedParagraph === 1 }"
            @click="selectParagraph(1)">
                {{ $t("assignment.answers.1") }}
            </p>
        </div>
        
        <button class="buttonConferma" @click="sendLanguage()">{{ $t("assignment.confirm") }}</button>
        <!--
        <div>
            <b-progress :value="value" :max="max" show-progress animated></b-progress>
            <b-progress class="mt-2" :max="max" show-value>
            <b-progress-bar :value="value * (6 / 10)" variant="success"></b-progress-bar>
            <b-progress-bar :value="value * (2.5 / 10)" variant="warning"></b-progress-bar>
            <b-progress-bar :value="value * (1.5 / 10)" variant="danger"></b-progress-bar>
            </b-progress>

            <b-button class="mt-3" @click="randomValue">Click me</b-button>
        </div>
        -->
    </body>
</template>
  
<script>
import router from '@/router';
import axios from "axios"
export default {
    data() {
        return {
            flag: null,
            selectedParagraph: null,
            phrase: null
        };
    },
    beforeCreate(){
        
    },
    created(){
        this.flag = this.$route.params.language;
        this.src = '../../flags/' + this.flag + ".png";
        this.fetchPhrase();
    },
    mounted() {
        
    },
    methods: {  
        fetchPhrase(){
        axios.get('http://localhost:5000/language')
        .then(response => {
          console.log(response.data);
          // do something with response.data
         this.phrase = response.data
        })
        .catch(error => {
          console.error(error);
        });
        },

        selectParagraph(index) {
        this.selectedParagraph = this.selectedParagraph === index ? null : index;
        },
        goBack(){
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
    width: 50%;
    height: 40px;
    text-align: center;
    margin-left: 25%;
    margin-top: 70%;
    background: #C3E986;
    border-radius: 10px;
    border-color: transparent;
}

.clickable-div {
  padding: 20px;
  margin: 10px;
  border-radius: 10px;
  background-color: rgb(188, 224, 149);
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.clickable {
    background-color: rgb(110, 229, 110);
}


.container{
    position:relative;
    margin:0cap;
}

img{
    position:absolute;
    display: inline;
    width:10%;
    right:0;
    margin-top: 1cap;
    margin-right: 1cap;
}
</style>

