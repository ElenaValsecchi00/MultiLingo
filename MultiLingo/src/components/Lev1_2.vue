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
            <p>{{ $t("assignment.header_1_2") }}</p>
            <p>{{ this.phrase }}</p>
            <button class="buttonAudio" @click="startListening()" :class="{'clickable': listening}">
            <img  class="audioImg"  
            :src="listening ? imageListening : imageNotListening">
            </button>
        </div>

        <div class="options">
            <div v-for="(name, index) in this.options">
                <p class="clickable-div" :class="{ 'clickable': selectedParagraph === index, 'wrongAnswer': selectedParagraph === index & wrongAnswer }"
                 @click="selectParagraph(index)">
                {{ name }}
            </p>
            </div>
        </div>
        
        <button class="buttonConferma" :disabled="disabledConfirm" @click="goOn()">{{ $t("assignment.confirm") }}</button>
    
    </body>
</template>
  
<script>
import router from '@/router';
import axios from "axios"

export default {
    data() {
        return {
            wrongAnswer: false,
            flag: null,
            selectedParagraph: null,
            phrase: null,
            options: null,
            listening: false,
            imageNotListening: '../../audio/volumedown.png',
            imageListening: '../../audio/volumeup.png',
            disabledConfirm: true
        };
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
        axios.get('http://127.0.0.1:5000/lev1/phrases',{params:{ex:"2"}})
        .then(response => {
        // do something with response.data
         let dict = response.data;
         this.phrase = dict['phrase']
         this.options = Object.keys(dict)
        .filter((key) => key!=='phrase')
        .reduce((obj, key) => {
            return Object.assign(obj, {
            [key]: dict[key]
            });
        }, {});
        })
        .catch(error => {
          console.error(error);
        });
        },
        selectParagraph(index) {
        this.selectedParagraph = this.selectedParagraph === index ? null : index;
        this.disabledConfirm = this.selectedParagraph === null? true : false;

        },
        checkAnswer(){
            const answer = this.options[this.selectedParagraph]
            axios.post('http://127.0.0.1:5000/lev1/ex1_2/check', {data: answer, ex: "2"})
            .then(response => { 
                console.log(response.data, answer)
                if (response.data) {
                    //if true the answer clicked was right
                    this.wrongAnswer = false
                }else{
                    //false the answer clicked was wrong
                    this.wrongAnswer = true
                }
            })
            .catch(error => {
                console.log(error)
            });
        },
        startListening(){
            this.listening = this.listening === false? true : false;
            axios.get('http://127.0.0.1:5000/lev1/pronounce')
            .then(response => {
                console.log(response.data)
                this.listening = false;
            })
            .catch(error => {
                console.error(error);
            });
        },
        goBack(){
        router.go(-1);
        },
        goOn(){
            this.checkAnswer()
            setTimeout(function(){router.push({name:"lev1_3", params: this.flag})}, 1000)
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

.buttonConferma:disabled{
    background-color: rgba(172, 160, 160, 0.806);
    cursor: not-allowed;
}

.buttonAudio{
    position:absolute;
    width: 50%;
    height: auto;
    text-align: center;
    left: 0; 
    right: 0; 
    margin-left: auto; 
    margin-right: auto; 
    background: #C3E986;
    border-radius: 10px;
    border-color: transparent;
    cursor: pointer;
}
.options{
    margin-top: 30vh;
}

.audioImg{
    width:50%;
}
.clickable-div {
  padding: 5px;
  margin: 10px;
  border-radius: 10px;
  background-color: rgb(188, 224, 149);
  cursor: pointer;
  transition: all 0.3s ease;
}

.clickable {
    background-color: rgb(6, 148, 6);
    transform: scale(0.95);
    transition: transform 0.5s ease;
}
.wrongAnswer{
    background-color: red;
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

