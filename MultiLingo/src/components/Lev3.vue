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
        
        <h3 class="text">{{ $t("assignment.header_3") }}</h3>
        
        <form>

        <div >
            <p class="textanswer">{{this.message}}</p>
        </div>
        <a href="#" v-on:click="getNextQuestion()" id="submit">SUBMIT</a>
        </form>
         <!--When pressed first time starts recording, when pressed second time stops-->
         <button class="buttonAudio" :disabled="disabledMic" @click="startRecordAudio" :class="{'clickable': recording}">
            <img  class="audioImg"  
            :src="recording ? imageRecording : imageNotRecording">
        </button>
        <h3 class="text" :class="{ 'hide': !seen }">{{ question }}</h3>
        <button class="buttonConferma" @click="get_result">{{ $t("assignment.confirm") }}</button>
      
    </body>
</template>


<script>
import router from '@/router';
import axios from "axios"
import i18n from '@/i18n';
export default {
    data() {
        return {
            flag: null,
            message: null,
            question: null,
            seen: false,
            language:null,
            recording: false,
            imageNotRecording: '../../micro/microphone.png',
            imageRecording: '../../micro/listening.png',
            recorder:null,
            disabledMic: false,
        };
    },
    created(){
        this.flag = this.$route.params.language;
        this.src = '../../flags/' + this.flag + ".png";
        this.language = i18n.global.locale.value;
    },
    mounted() {
        
    },
    methods: {  
        goBack(){
            router.go(-1);
        },
        getNextQuestion(){
            axios.post('http://127.0.0.1:5000/lev3/conversation', {data: this.message})
            .then(response => { 
                console.log(response.data)
                this.question = response.data
                this.seen = true
            })
            .catch(error => {
                console.log(error)
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
                this.message = response.data
                this.disabledConfirm = false
            })
            .catch(error => {
                console.log(error)
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

#submit{
    text-align: center;
    padding:150px;
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


.text{
    width: auto;
    height: auto;
    background-color: #C3E986;
    border-radius: 10px;
    font-size: 20px;
    margin: 20px;
    padding: 10px;
}

.textanswer{
    width: auto;
    height: 7vh;
    background-color: white;
    font-size: smaller;
    text-align: center;
    border-radius: 10px;
    font-size: 20px;
    margin: 20px;
    padding: 10px;
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

.hide{
    visibility: hidden !important;
}

</style>
