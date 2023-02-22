import { calcHeight } from "./calcHeight.js";
import { get } from "./get.js";
import "./userInteraction.js"
import "./pressSpace.js"

const height = calcHeight();
const textContent = get('#text-content');
textContent.style.margin = `${height -15}px 0 0 0`;

