export const get = (selection)=>{
    const el = document.querySelector(selection);

    if(el) return el;
    else throw new ArgumentException("your selection does not exist");
};