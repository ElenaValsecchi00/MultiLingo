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
            <p>{{ $t("assignment.header_2_2") }}</p>

            <button class="buttonAudio speaker" @click="startListening()" :class="{'clickable': listening}">
            <img  class="audioImg"  
            :src="listening ? imageListening : imageNotListening">
            </button>
            <p class="text" >{{this.message}}</p>
            <p>Errors: {{this.numerrors}}, {{this.errors}}</p>
        </div>
        
        <!--When pressed first time starts recording, when pressed second time stops-->
        <button class="buttonAudio mic" :disabled="disabledMic" @click="startRecordAudio" :class="{'clickable': recording}">
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
            message:null,
            flag: null,
            listening: false,
            recording: false,
            imageNotListening: '../../audio/volumedown.png',
            imageListening: '../../audio/volumeup.png',
            imageNotRecording: '../../micro/microphone.png',
            imageRecording: '../../micro/listening.png',
            disabledMic: true,
            disabledConfirm: true,
            score: 0,
            errors: null,
            numerrors: 0
        };
    },

    created(){
        this.flag = this.$route.params.language;
        this.src = '../../flags/' + this.flag + ".png";
        
    },
    mounted() {
        
    },
    methods: {  
        startListening(){
            this.disabledMic = false
            this.listening = this.listening === false? true : false;
            axios.get('http://127.0.0.1:5000/lev2/pronounce')
            .then(response => {
                console.log(response.data)
                this.listening = false;
                
            })
            .catch(error => {
                console.error(error);
            });
        },
        //function that prompts backend to record and gets the speech to text
        startRecordAudio(){
            this.recording = true;
            axios.post('http://127.0.0.1:5000/lev3/record')
            .then(response => { 
                this.stopRecordAudio()
            })
            .catch(error => {
                console.log(error)
            });
        },  
        stopRecordAudio(){
            this.recording = false;
            axios.get('http://127.0.0.1:5000/lev3/conversation')
            .then(response => { 
                console.log(response.data)
                this.disabledConfirm = false;
                this.message = response.data["data"];
                this.errors = response.data["errors"];
                this.numerrors = response.data["numerrors"]
            })
            .catch(error => {
                console.log(error)
            });
        },
        goBack(){
        router.go(-1);
        },
        goOn(){
            //***where*** 
            setTimeout(function(){router.replace({name:"result1", params: this.flag})}, 1000)
        }
    }
    };
</script>

<style scoped>
body{
    background-color: #FBF2D4;
}

.text{
    width: 320;
    height: auto;
    background-color: white;
    border-radius: 10px;
    margin: 160px 10px 2px 10px;
    font-size: 20px;
    padding: 20px;
   
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

.mic{
    bottom:100px;
}

.speaker{
    bottom:500px;
}

.buttonAudio:disabled{
    background-color: rgba(172, 160, 160, 0.806);
    cursor: not-allowed;
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

