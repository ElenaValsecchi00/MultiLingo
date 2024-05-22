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
            <p>{{ $t("assignment.header_1_1") }}</p>
            <p>{{ this.phrase }}</p>
        </div>
        <div class="options">
            <div v-for="(name, index) in this.options">
                <p class="clickable-div" :class="{ 'clickable': selectedParagraph === index }"
                 @click="selectParagraph(index)">
                {{ name }}
            </p>
            </div>
        </div>
        <!--When pressed first time starts recording, when pressed second time stops-->
        <button class="buttonAudio" :disabled="disabledMic" @click="startRecordAudio" :class="{'clickable': recording}">
            <img  class="audioImg"  
            :src="recording ? imageRecording : imageNotRecording">
        </button>
        
        <button class="buttonConferma" :disabled="disabledConfirm" @click="goOn()">{{ $t("assignment.confirm") }}</button>
    
        
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
            recording: false,
            imageNotRecording: '../../micro/microphone.png',
            imageRecording: '../../micro/listening.png',
            recorder:null,
            disabledMic: true,
            disabledConfirm: true,
            score: 0
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
        axios.get('http://127.0.0.1:5000/lev1/phrases', {params:{ex:"1"}})
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
        this.disabledMic = this.selectedParagraph === null? true : false;
        },

        goBack(){
        router.go(-1);
        },
        //function that prompts backend to record and gets the speech to text
        startRecordAudio(){
            this.recording = true;
            const answer = this.options[this.selectedParagraph]
            axios.post('http://127.0.0.1:5000/lev1/ex1/audio', {data: answer})
            .then(response => { 
                console.log(response.data, answer)
                if (response.data) {
                    this.score += 0.5
                }
                this.stopRecordAudio()
            })
            .catch(error => {
                console.log(error)
            });
        }, 
        stopRecordAudio(){
            this.recording = false;
            axios.get('http://127.0.0.1:5000/lev1/ex1/audio')
            .then(response => { 
                console.log(response.data)
                if(response.data){
                    console.log("tutto corretto")
                    this.score += 0.5
                    console.log(this.score)
                }
                
                this.disabledConfirm = false
            })
            .catch(error => {
                console.log(error)
            });
        },
        goOn(){
            router.push({name:"ex2", params: this.flag})
        }
    }
    };
</script>

<style scoped>
body{
    background-color: #FBF2D4;
}

.options{
    overflow: scroll;
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
.buttonAudio:disabled{
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
    bottom:100px;
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

