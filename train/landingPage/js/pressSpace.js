import { get } from "./get.js";

let status = "stop";
let min = 0;
let sec = 0;
let ms = 0;
let millisecInterval, secondInterval, minInterval;
function StartTimer(){

     millisecInterval = setInterval(()=>{
       ms = (ms > 1000) ? 1 : (ms +1);
       UITimer(min, sec, ms);
    },1);

    secondInterval = setInterval(()=>{
       sec = (sec > 59) ? 1 : (sec +1);

    },1000);

    minInterval = setInterval(()=>{
       min = (min > 59) ? 1 : (min +1);

    },1000 * 60);
}

function StopTimer(){
    clearInterval(millisecInterval);
    clearInterval(secondInterval);
    clearInterval(minInterval);
    min =0;
    sec= 0;
    ms = 0;
}

new Date().get
function UITimer(min, sec, ms){
    const minutes = get('.minutes');
    const seconds = get('.seconds');
    const milliseconds = get('.milliseconds');
    min = min.toString().length == 1? `0${min}`: ` ${min}`;
    sec = sec.toString().length == 1? ` 0${sec}`: ` ${sec}`;
    ms = ms.toString().length == 2? ` 0${ms}`: ` ${ms}`;
    minutes.textContent = min;
    seconds.textContent = sec;
    milliseconds.textContent =  ms;
}
function startHotLap(){
        StartTimer();
        const startBtn = get('.space');
        console.log("you started a hot lap");
        startBtn.style.background = `#fff`;
        startBtn.style.color = `#333`;
        startBtn.textContent = `Press Space To Stop`;
        status = "start";
};
function  stopHotLap(){
        StopTimer();
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



