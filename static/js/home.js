function appear_delete_button(id){
    let btn_delete = document.getElementById(id).nextSibling
    btn_delete.style.animation = 'appear 3s ease-out forward';
    console.log(btn_delete)
    // btn_delete.style.opacity = '1';
}

function disappear_delete_button(id){
    let btn_delete = document.getElementById(id).nextElementSibling
    btn_delete.style.animation = 'disappear 3s ease-out forward';

}

