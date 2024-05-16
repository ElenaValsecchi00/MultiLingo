<template>
    <body>
        <header>
            <div class="container">
                <button @click="goBack()" class="back_button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8"/>
                </svg>
                </button>
                <img :src="src" class="flag" alt="flag">
            </div>
            
        </header>
        <div>
            <p>{{ $t("assignment.header") }}</p>
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
        <button class="buttonAudio" @click="recordAudio()" :class="{'clickable': recording}">
            <img  class="audioImg"  
            :src="imageUrl">
        </button>
        
        <button class="buttonConferma" @click="sendLanguage()">{{ $t("assignment.confirm") }}</button>
    
        
    </body>
</template>
  
<script>
import router from '@/router';
import axios from "axios"
import {FFmpeg} from '@ffmpeg/ffmpeg';

export default {
    data() {
        return {
            flag: null,
            selectedParagraph: null,
            phrase: null,
            options: null,
            recording: false,
            imageUrl: '../../micro/microphone.png',
            recorder:null
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
        axios.get('http://127.0.0.1:5000/lev1/ex1')
        .then(response => {
        // do something with response.data
         let dict = response.data;
         console.log(dict)
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
        //start or stops a recording depending on the state of the button
        recordAudio(){
            this.recording = (this.recording==true)?false:true;
            this.imageUrl= "../../micro/listening.png";
            (async () => {
            if(this.recording==true){
                this.recorder = await this.record();
                this.recorder.start();
            }
            else{
                const audio = await this.recorder.stop();
                audio.play();
                let formData = new FormData();
                formData.set("audio", audio.audioFile);
                this.sendAudio(formData);
                
            }
            })();
        },
        //function that provides start stop functionalities 
        record(){
            return new Promise(resolve => {
                navigator.mediaDevices.getUserMedia({ audio: true })
                .then(stream => {
                    const mediaRecorder = new MediaRecorder(stream);
                    const audioChunks = [];
                    mediaRecorder.addEventListener("dataavailable", event => {
                    audioChunks.push(event.data);
                    });

                    const start = () => {
                    mediaRecorder.start();
                    };

                    const stop = () => {
                    return new Promise(resolve => {
                        mediaRecorder.addEventListener("stop", () => {
                        const audioBlob = new Blob(audioChunks);
                        const audioWAVBlob = this.convertWebmToWAV(audioBlob);
                        const audioFile = new File([audioWAVBlob], "yourfilename.wav");
                        const audioUrl = URL.createObjectURL(audioBlob);
                        const audio = new Audio(audioUrl);
                        const play = () => {
                            audio.play();
                        };

                        resolve({ audioWAVBlob, audioUrl, play, audioFile });
                        });

                        mediaRecorder.stop();
                    });
                    };

                    resolve({ start, stop });
                });
            });
        },
        //function that converts the webm audio blob to wav 
        async convertWebmToWAV(webmBlob){
            const ffmpeg = new FFmpeg();
            await ffmpeg.load({ baseURL: 'node-modules/@ffmpeg/core@0.12.6/dist/umd'});

            const inputName = 'input.webm';
            const outputName = 'output.wav';

            ffmpeg.FS('writeFile', inputName, await fetch(webmBlob).then((res) => res.arrayBuffer()));

            await ffmpeg.run('-i', inputName, outputName);

            const outputData = ffmpeg.FS('readFile', outputName);
            const outputBlob = new Blob([outputData.buffer], { type: 'audio/wav' });

            return outputBlob;
        },  
        
        //handle send audio to api and the transcription
        sendAudio(audioFile){
            axios.post('http://127.0.0.1:5000/lev1/ex1/audio', audioFile)
            .then(response => { 
                console.log(response)
                this.getTextfromAudio()
            })
            .catch(error => {
                console.log(error)
            });
        },
        getTextfromAudio()
        {
            axios.get('http://127.0.01:5000/lev1/ex1/audio')
            .then(response => { 
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            });
        },
        callback (msg) {
            console.debug('Event: ', msg)
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

