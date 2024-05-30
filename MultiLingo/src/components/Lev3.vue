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
        <div class="scrollable"> 
            <h3 class="text">{{ $t("assignment.header_3") }}</h3>
            <div v-for="(name, index) in this.conversation">
                <h3 class="text" :class="{ 'answer': index % 2 == 0}">{{ name }}</h3> 
            </div>
        </div>
        
        <div class="message">
            <form>
            <p class="textanswer" >{{this.message}}</p>
            <a href="#" v-on:click="getNextQuestion()" id="submit">SUBMIT</a>
            </form>
        </div>
        <!--When pressed first time starts recording, when pressed second time stops-->
        <button class="buttonAudio" @click="startRecordAudio()" :class="{'clickable': recording}">
            <img  class="audioImg"  
            :src="recording ? imageRecording : imageNotRecording">
        </button>
        
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
            conversation: null 
        };
    },
    created(){
        this.flag = this.$route.params.language;
        this.src = '../../flags/' + this.flag + ".png";
        this.language = i18n.global.locale.value;
        this.conversation = [];
    },
    mounted() {
        
    },
    methods: {  
        goBack(){
            router.go(-1);
        },
        getNextQuestion(){
            this.conversation.push(this.message)
            axios.post('http://127.0.0.1:5000/lev3/conversation', {data: this.message})
            .then(response => { 
                console.log(response.data)
                this.conversation.push(response.data)
                router.go(-1);
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
                this.disabledConfirm = false;
                this.message = response.data;
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

#submit{
    text-align: right;
    position: relative;
    left: 250px;
    bottom:45px;
}

.audioImg{
    width:30%;
}
.scrollable{
    height:400px;
    overflow: auto;
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
    font-size: small;
    text-align: left;
    width: 250px;
    height: 70px;
}
.answer{
    background-color: white;
    position:left;
}
.buttonAudio{
    position:absolute;
    width: 50%;
    height: auto;
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
.clickable {
    background-color: rgb(6, 148, 6);
    transform: scale(0.95);
    transition: transform 0.5s ease;
}

.audioImg{
    width:50%;
}

.hide{
    visibility: hidden !important;
}

.message{
    background-color: white;
    border-radius: 10px;
    width: 315px;
    height: 70px;
    margin: 20px;
    position:absolute;
    bottom: 130px;
    display: inline-flex;
}

</style>
