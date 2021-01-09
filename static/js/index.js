const openBtn = document.getElementById('openBtn')
const popup= document.getElementById('popup')
const closeBtn = document.getElementById('closeBtn')

openBtn.addEventListener('click',() =>{
    popup.style.display='inline'
})

closeBtn.addEventListener('click', ()=>{
    popup.style.display='none'
})