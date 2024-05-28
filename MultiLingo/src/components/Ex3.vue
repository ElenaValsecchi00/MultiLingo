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
        
        <p>{{ $t("assignment.header_1_3") }}</p>
        
        
       
        <div class="text">
            <button class="buttonAudio" @click="startListenAudio()" :class="{'clickable': speaking}">
            <img  class="audioImg"  
                :src="speaking ? imageSpeaking : imageNotSpeaking">
            </button>
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
            flag: null,
            selectedParagraph: null,
            phrase: null,
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
          console.log(response.data);
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
        //Check if the guessed phrase is correct
        get_result(){
            axios.post('http://127.0.0.1:5000/lev1/ex3/answer', {phrase:this.guessedPhrase})
            .then(response => {
            console.log(response.data);
            })
            .catch(error => {
            console.error(error);
            });
        },
        selectParagraph(index) {
        this.selectedParagraph = this.selectedParagraph === index ? null : index;
        this.chooseOption(index);
        },
        chooseOption(word){
            this.guessedPhrase+=this.options[word]+" ";
            delete this.options[word];
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
    position:relative;
    width: 10%;
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

.inputText{
    padding:20px;
    margin-top:15vh;

}

.text{
    width: auto;
    height: 35vh;
    background-color: white;
    border-radius: 10px;
    font-size: 20px;
    
}

</style>
