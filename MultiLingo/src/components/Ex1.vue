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
export default {
    data() {
        return {
            flag: null,
            selectedParagraph: null,
            phrase: null,
            options: null,
            recording: false,
            imageUrl: '../../micro/microphone.png'
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
        axios.get('http://127.0.0.1:5000/ex1')
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
        
        recordAudio(){
            this.recording = true;
            this.imageUrl= "../../micro/listening.png"
            const sleep = time => new Promise(resolve => setTimeout(resolve, time));

            (async () => {
            const recorder = await this.record();
            recorder.start();
            await sleep(3000);
            const audio = await recorder.stop();
            audio.play();
            })();
        },
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
                        const audioUrl = URL.createObjectURL(audioBlob);
                        const audio = new Audio(audioUrl);
                        const play = () => {
                            audio.play();
                        };

                        resolve({ audioBlob, audioUrl, play });
                        });

                        mediaRecorder.stop();
                    });
                    };

                    resolve({ start, stop });
                });
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

