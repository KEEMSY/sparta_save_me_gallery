

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    comment_check();
    initial_underline()
});

function comment_check(){
    let comment_list = document.getElementsByClassName('comment_info')
    for(let i = 0; i<comment_list.length; i ++){
        let title = comment_list[i].children[1].innerText.split('<br/>')[0].slice(0,10)
        comment_list[i].children[0].children[0].innerText = title
        comment_list[i].children[1].innerHTML = comment_list[i].children[1].innerText
    }

}



function open_write_box(){
    document.getElementById('modal_container').style.display = 'block'
    document.getElementById('modal_container').style.animation = 'modal_appear 0.5s ease-out forwards'
}

function close_write_box(){
    document.getElementById('comment_name').value = ''
    document.getElementById('comment_password').value = ''
    document.getElementById('comment_content').value = ''
    document.getElementById('modal_container').style.animation = 'modal_disappear 1s ease-out forwards'
    setTimeout(function (){
         document.getElementById('modal_container').style.display = 'none'
    },1000)


}

function save_comment(){
    let username = document.getElementById('comment_name').value
    let pwd = document.getElementById('comment_password').value
    let comment = document.getElementById('comment_content').value

    if(username === '' || pwd==='' || comment === ''){
        return alert('Name 과 Password는 필수 입력사항입니다~')

    }

    comment = comment.replace(/(?:\r\n|\r|\n)/g, '<br/>');
    $.ajax({
        type: 'POST',
        url: '/comments/',
        data: {
            'username': username,
            'password': pwd,
            'comment': comment,
        },
        success: function(response){
            console.log(response['msg'])
        }
    })

    window.location.href='/comments/';
}

function open_delete_comment_box(id){
     $('body,html').animate({scrollTop:0},1000)
    window.scrollTo(0,0)
    document.getElementById('modal_delete_container').style.display='block'
    document.getElementById('modal_delete_container').style.animation = 'modal_appear 0.5s ease-out forwards'
    document.getElementById('delete_target').innerText = id.split('_')[1]
    let name = document.getElementById('comment_user_name_' + id.split('_')[1]).innerText
    document.getElementById('check_comment_name').value = name
}

function close_delete_comment_box(){

    document.getElementById('check_comment_name').value=''
    document.getElementById('check_comment_password').value=''
    document.getElementById('delete_target').innerText=''
    document.getElementById('modal_delete_container').style.animation = 'modal_disappear 0.5s ease-out forwards'
    setTimeout(function (){
         document.getElementById('modal_delete_container').style.display='none'
    },1000)
}

function delete_comment(){
    let username = document.getElementById('check_comment_name').value
    let password = document.getElementById('check_comment_password').value
    let target_id = document.getElementById('delete_target').innerText
    let comment = document.getElementById('comment_content_' + target_id).innerText

    comment = comment.replace(/(?:\r\n|\r|\n)/g, '<br/>');

    $.ajax({
        type: 'POST',
        url: '/comments/delete/',
        data: {
            'username': username,
            'password': password,
            'id': target_id,
        },
        success: function(response){
            console.log(response['msg'])
        }
    })
    location.reload();
}

