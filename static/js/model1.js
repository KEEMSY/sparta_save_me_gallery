function appear(id){
    let target = document.getElementById(id)
    let modal = target.children[0]
    modal.style.display = 'flex'
    target.style.transform = 'scale(1.1)'
    target.style.zIndex='2'
}

function disappear(id){
    let target = document.getElementById(id)
    let modal = target.children[0]
    modal.style.display = 'none'
    target.style.transform = 'scale(1)'
    target.style.zIndex='0'
}



function move_to_upload(){
    window.scrollTo(0, 1300)
    console.log(value)

    window.addEventListener('scroll', function(){
    let value =window.scrollY
    console.log(value)
})
}