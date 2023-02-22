import { get } from "./get.js";

const lineOne = get('#lineOne').getBoundingClientRect().bottom;
const navHeight = get('#nav-bar').getBoundingClientRect().height;
export const calcHeight = ()=>{
    return lineOne - navHeight;
};