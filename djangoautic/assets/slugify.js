const titleInput = document.querySelector('input[name=title]')
const sluginput = document.querySelector('input[name=slug]')

const slugify = (val) =>{
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-') //replace & '-and-'
    .replace(/[\s\W-]+/g, '_') //replace spaces, non word chars and dashes with a single dash

};


titleInput.addEventListener('keyup',(e)=>{
    sluginput.setAttribute('value', slugify(titleInput.value));
})
