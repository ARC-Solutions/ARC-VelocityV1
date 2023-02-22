//if('addEventListener' in document){
//    document.addEventListener('DOMContentLoad', ()=>{
//       FastClick.attach(document.body); // 300ms delay between physical tap and the firing of a click event
//    }, false);
//}

//send a request to switch on the GPIOs
const switchOn = (direction)=>{
    fetch('http://localhost:5000/' + direction)
    .then(res => res.text())
    .then(res => console.log(res))
    .catch(err => console.log(err));
}

const switchOff = (direction)=>{
    fetch('http://localhost:5000/' + direction + '-off')
        .then(res => res.text())
        .then(res => console.log(res))
        .catch(error => console.log(error));
}

//binding the buttons on the UI
const buttons = ['forward', 'backward', 'left', 'right'];
let arrowKeys;
let htmlTags;
buttons.forEach(btn =>{
 arrowKeys = document.querySelector(`.${btn}`);
 htmlTags = [...document.querySelectorAll(`.controlls`)];

 // switches on on mousedown
 arrowKeys.addEventListener('mousedown', ()=>{
    switchOn(btn);
 });

 //switches off on mouseup
 arrowKeys.addEventListener("mouseup", ()=>{
    switchOff(btn);
 })
});

// keeping track which keys are down
const keysDown = {
    up:false,
    down:false,
    left: false,
    right: false
}

//map the keys to the directions+
const keyDirections = {
    up: 'forward',
    down: 'backward',
    left: 'left',
    right: 'right'
}
console.log(htmlTags);
//bind the keyboard keys
const directions = ['up', 'down', 'left', 'right'];
const wasdDirection = ['w','a','s','d'];

const animateArrows = (key)=>{
    if(key == 'up' || key == 'w'){
        htmlTags[0].classList.add("animate");
    }
    else if(key == 'right' || key == 'd'){
        htmlTags[1].classList.add("animateX");
    }
    else if(key == 'down' || key == 's'){
        htmlTags[2].classList.add("animate");
    }
    else if(key == 'left' || key == 'a'){
        htmlTags[3].classList.add("animateX");
    }
}
// arrow keys
directions.map((key, index)=>{
    Mousetrap.bind(key, ()=>{
        if(!keysDown[key]){
            keysDown[key] = true;
            animateArrows(key);
            console.log(htmlTags[0]);
            switchOn(keyDirections[key]);
            
            console.log(`you pressed ${key} and switched on`);
        }
    }, 'keydown');

    Mousetrap.bind(key, ()=>{
            keysDown[key] = false;
            switchOff(keyDirections[key]);
            htmlTags.forEach(tag =>{
                tag.classList.remove("animate");
                tag.classList.remove("animateX");
            })
            htmlTags[index].classList.remove("animate");
            console.log(`you lift the ${key} key and switched off`);
    }, 'keyup')
});

//WASD
wasdDirection.forEach(key =>{

    //switch on on keydown
    Mousetrap.bind(key, ()=>{
        let translateKey;
        if(!keysDown[key]){
            keysDown[key] = true;
            translateKey = key === 'w'? 'up': key === 'a' ? 'left': key === 'd' ? 'right': key === 's' ? 'down':''; // translates the wasd key to the arrow keys
            animateArrows(key);
            switchOn(keyDirections[translateKey]);
            console.log(`you pressed ${key} and switched on`);
        }
    },'keydown');

    //switch off on keyup
    Mousetrap.bind(key, ()=>{
        let translateKey;
            keysDown[key] = false;
           translateKey = key === 'w'? 'up': key === 'a' ? 'left': key === 'd' ? 'right': key === 's' ? 'down':''; // translates the wasd key to the arrow keys
            htmlTags.forEach(tag =>{
                tag.classList.remove("animate");
                tag.classList.remove("animateX");
            })
            switchOff(keyDirections[translateKey]);
            console.log(`you lift the ${key} key and switched off`);
    },'keyup');
});