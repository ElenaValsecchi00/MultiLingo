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
            <p>{{ $t("assignment.header_1_3") }}</p>
        </div>
        <!--When pressed first time starts recording, when pressed second time stops-->
        <button class="buttonAudio" :disabled="disabledMic" @click="startListenAudio" :class="{'clickable': listening}">
            <img  class="audioImg"  
            :src="speaking ? imageSpeaking : imageNotSpeaking">
        </button>
        <div class="options">
            <div v-for="(name, index) in this.options">
                <p class="clickable-div" :class="{ 'clickable': selectedParagraph === index }"
                 @click="selectParagraph(index)">
                {{ name }}
            </p>
            </div>
        </div>
        <button class="buttonConferma" @click="sendLanguage()">{{ $t("assignment.confirm") }}</button>
      
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
            imageNotSpeaking: '../../speaker/speaker.jpg',
            imageSpeaking: '../../speaker/speaker-talking.jpg'
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
        axios.get('http://127.0.0.1:5000/lev1/ex3')
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

        selectParagraph(index) {
        this.selectedParagraph = this.selectedParagraph === index ? null : index;
        },
        goBack(){
        router.go(-1);
        },
        startListenAudio(){
            this.recording = true;
            //Actually pornounce sentence
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
}

.clickable-div {
  width: fit-content;
  padding: 5px;
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
