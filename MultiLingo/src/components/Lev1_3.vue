<template>
    <body>
        <header>
            <div class="container">
                <button @click="goBack()" class="back_button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                </svg>
                </button>
                <img :src="src" class="flag"  alt="flag">
            </div>      
        </header>
        <div>
            <p>{{ $t("assignment.header_1_3") }}</p>
            <button class="buttonAudio" @click="startListenAudio()" :class="{'clickable': speaking}">
            <img  class="audioImg"  
            :src="speaking ? imageSpeaking : imageNotSpeaking">
            </button>
        </div>
       
        
        <div class="options inputText text">
            <div v-for="(name, index) in this.optionsChosen">
                <p class="clickable-div" @click="removeOption(index)">
                {{ name }}
            </p>
        </div>
            <!--<p class="text" :class="{'wrongAnswer': wrongAnswer}">{{guessedPhrase}}</p>-->
        </div>
        <div class="options">
            <div v-for="(name, index) in this.options">
                <p class="clickable-div" @click="addOption(index)">
                {{ name }}
            </p>
            </div>
        </div>
        <button class="buttonConferma" @click="get_result">{{ $t("assignment.confirm") }}</button>
      
    </body>
</template>


<script>
import router from '@/router';
import axios from "axios"
export default {
    data() {
        return {
            wrongAnswer: null,
            flag: null,
            selectedParagraph: null,
            selectedParagraphChosen: null,
            phrase: null,
            optionsChosen: [],
            options: null,
            speaking: false,
            imageNotSpeaking: '../../audio/volumedown.png',
            imageSpeaking: '../../audio/volumeup.png',
            guessedPhrase:""
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
        axios.get('http://127.0.0.1:5000/lev1/phrases',{params:{ex:"3"}})
        .then(response => {
        // do something with response.data
        this.options = Object.values(response.data)
        this.phrase = response.data["phrase"]
        this.options.pop(this.phrase)
        })
        .catch(error => {
          console.error(error);
        });
        },
        //Check if the guessed phrase is correct
        get_result(){
            this.optionsChosen.forEach((value) => {
                this.guessedPhrase += value + " "
            });
            console.log(this.guessedPhrase)
            axios.post('http://127.0.0.1:5000/lev1/ex3/answer', {phrase:this.guessedPhrase})
            .then(response => {
                console.log(response.data)
                if(response.data){
                    //the answer was correct
                    this.wrongAnswer = false
                }
                else{
                    //mistakes were made
                    this.wrongAnswer = true
                }
            })
            .catch(error => {
                console.error(error);
            });
            this.goOn();
            
        },
        addOption(index) {
            let word = this.options[index]
            this.optionsChosen.push(word)
            this.options.splice(index,1);
        },
        removeOption(index){
            this.options.push(this.optionsChosen[index])
            this.optionsChosen.splice(index,1);
        },
        goBack(){
        router.go(-1);
        },
        startListenAudio(){
            this.speaking = true;
            //Actually pronounce sentence
            axios.get('http://127.0.0.1:5000/lev1/pronounce')
            .then(response => {
                console.log(response.data)
                this.speaking= false;
            })
            .catch(error => {
                console.error(error);
            });
            },
        goOn(){
            setTimeout(function(){router.replace({name:"result1", params: this.flag})}, 1000)
        }
        }
    };

</script>

<style scoped>
body{
    background-color: #FBF2D4;
}

.options{
    
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
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
.audioImg{
    width:50%;
}

.clickable-div {
  padding: 5px;
  margin: 5px;
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
.wrongAnswer{
    background-color: rgb(255, 0, 0);
}
.inputText{
    padding:20px;
    margin-top:15vh;

}
.text{
    width: 330px;
    height: auto;
    margin-left: 15px;
    background-color: white;
    border-radius: 10px;
    font-size: 20px;
    
}

</style>