import { get } from "./get.js";

let status = "stop";
let min = 0;
let sec = 0;
let ms = 0;
const minutes = get('.minutes');
const seconds = get('.seconds');
const milliseconds = get('.milliseconds');
let interval;
function StartTimer(){
    ms++;
    if(ms <= 9){
    ms = ms.toString().length == 1? `0${ms}`: `${ms}`;
    milliseconds.textContent =  ms;
    }
    
    if(ms> 9){
        milliseconds.textContent =  ms;
    }
    
    if(ms>99){
        sec++;
        sec = sec.toString().length == 1? `0${sec}`: `${sec}`;
        seconds.textContent = sec;
        ms = 0;
    }
    if(sec >= 9){
        seconds.textContent = sec;
    }
    
    if(sec >= 60){
        min++;
        min = min.toString().length == 1? `0${min}`: `${min}`;
        minutes.textContent = min;
        sec = 0;
        seconds.textContent = sec;
    }

}
function resetUI(){
    min = 0;
    sec = 0;
    ms = 0;
    min = min.toString().length == 1? `0${min}`: `${min}`;
    sec = sec.toString().length == 1? `0${sec}`: `${sec}`;
    ms = ms.toString().length == 1? ` 0${ms}`: `${ms}`;
    minutes.textContent = min;
    seconds.textContent = sec;
    milliseconds.textContent = ms;
}
function startHotLap(){
    resetUI();  
        interval = setInterval(StartTimer, 10);
        const startBtn = get('.space');
        console.log("you started a hot lap");
        startBtn.style.background = `#fff`;
        startBtn.style.color = `#333`;
        startBtn.textContent = `Press Space To Stop`;
        status = "start";
};

function  stopHotLap(){

        clearInterval(interval);

        min = 0;
        sec = 0;
        ms = 0;
        const startBtn = get('.space');
        console.log("you finished your lap");
        startBtn.style.background = `var(--primary-color)`;
        startBtn.style.color = `#fff`;
        startBtn.textContent = `Press Space To Start`;
        status = "stop";
};

Mousetrap.bind('space', ()=>{
    if(status == "stop"){
        startHotLap();

    }
    else if(status == "start"){
        stopHotLap();
    }
}, 'keydown');



