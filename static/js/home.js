$(document).ready(function () {
    initial_underline()
});

function appear_delete_button(id){
    let btn_delete = document.getElementById(id).nextElementSibling
    btn_delete.style.animation = "appear 1s ease-out forwards";
    btn_delete.style.zIndex = '3';
}

function disappear_delete_button(id){
    let btn_delete = document.getElementById(id)
    btn_delete.style.animation = 'disappear 1s ease-out forwards';
    btn_delete.style.zIndex = '1';
}


window.addEventListener('scroll', function(){
    let value = window.scrollY;
    for(let i=0;i<3;i++){
        animation_on(i, value )
    }
    let up_box = document.getElementById('up_button')
    if(value >= 100){
        up_box.style.display = 'block'

    }
    else{
        up_box.style.display = 'none'
    }

})

function animation_on(row, value){
    if(value>=1300+ row * 900){
        let content = document.getElementsByClassName('content')[row]
        content.style.animation = 'slide_top 1s ease-out forwards'
    }
    else if(value>=500+ row * 300){
        let content = document.getElementsByClassName('content')[row]
        content.style.animation = 'slide_down 1s ease-out forwards'
    }

    if(value >=1300 + row * 900){
        let content = document.getElementsByClassName('content')[row+3]
        content.style.animation = 'slide_top 1s ease-out forwards'
    }
    else{
        let content = document.getElementsByClassName('content')[row+3]
        content.style.animation = 'slide_down 1s ease-out forwards'
    }
}


function delete_option(id){
    let box_id = 'delete_check_box_' + id
    let target =   document.getElementById(box_id).style.display
    if(target ==='block'){
        document.getElementById(box_id).style.display='none'
    }
    else{
        document.getElementById(box_id).style.display='block'
        document.getElementById('info_home_'+id).style.display = 'none'

    }

}

function close_delete_option(id){
    let box_id = 'delete_check_box_' + id
    document.getElementById(box_id).style.display='none'

}

function delete_masterpiece_final(id){
    let password_tag = document.getElementById('home_password_'+ id)
    let password = password_tag.value

    console.log('delete id is : ' ,id)
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            'id': id,
            'password': password
        },
        success: function(response){
            console.log(response['msg'])
        }
    })

    close_delete_option(id)
    password_tag.value = ''
    window.location.reload();
}

function info_option(id){
    let box = document.getElementById('info_home_'+id)
    let box_id = 'delete_check_box_' + id

    if(box.style.display==='none'){
        box.style.display = 'block';
        document.getElementById(box_id).style.display = 'none'

    }
    else{
        box.style.display = 'none'
    }

}

function green_option(id){
    close_delete_option(id)
    document.getElementById('info_home_'+ id).style.display = 'none'
    console.log('greeennn!')
}

var content_list = document.querySelectorAll('div.content')

content_list.forEach((content)=>content.addEventListener('mouseleave',(e)=>off_all_option(e)))


function off_all_option(e){
    console.log('off_function in!')
    console.log(e.fromElement.id)
    close_delete_option(e.fromElement.id)
    document.getElementById('info_home_'+e.fromElement.id).style.display = 'none'
}

