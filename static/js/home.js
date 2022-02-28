function appear_delete_button(id){
    let btn_delete = document.getElementById('delete_'+ id.split('_')[1])
    btn_delete.style.animation = "appear 1s ease-out forwards";
}

function disappear_delete_button(id){
    let btn_delete = document.getElementById(id).nextElementSibling
    btn_delete.style.animation = 'disappear 1s ease-out forwards';

}


window.addEventListener('scroll', function(){
    let value = window.scrollY;
})

let content_list = document.querySelectorAll('div.content')

content_list.forEach((parts)=>
    parts.addEventListener('mouseover',(e)=> up_animation(e)))
function up_animation(e){
    console.log('function on!')
    console.log(e.currentTarget.scrollY)
}
