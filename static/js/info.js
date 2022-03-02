$(document).ready(function () {
    initial_underline()
});

var develop_profile = document.querySelectorAll('div.developer_profile')

window.addEventListener('scroll',function(){
    let value = window.scrollY;
    for(let i =0; i<develop_profile.length; i++){
        profile_animation_on(i, value)
    }

    let up_box = document.getElementById('up_button')
    if(value >= 100){
        up_box.style.display = 'block'
    }
    else{
        up_box.style.display = 'none'
    }
})



function profile_animation_on(row, value){
    if(value>=500 + row * 500){
        develop_profile[row].style.animation = 'slide_top 1s ease-out forwards'
    }
    else{
        develop_profile[row].style.animation = 'slide_down 1s ease-out forwards'
    }
    if(value >=1100 + row * 700){
        develop_profile[row].style.animation = 'slide_top 1s ease-out forwards'
    }
    else{
        develop_profile[row].style.animation = 'slide_down 1s ease-out forwards'
    }
}