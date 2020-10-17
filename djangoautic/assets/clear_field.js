const commentInput = document.querySelector('input[name=comment_input]')

commentInput.addEventListener('focus',(e)=>{
    commentInput.setAttribute('value','')
})