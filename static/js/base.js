/* csrf 토큰 관련 */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/* 언더바 */

let underline = document.getElementById('under_bar')
let menu_list = document.querySelectorAll('.nav_context_box a')
console.log(underline)
console.log(menu_list)

menu_list.forEach((menu)=>
    menu.addEventListener('mouseover ',(e)=> indicator(e)))

function indicator(e){
    console.log('event on!')
    underline.style.left=e.currentTarget.offsetLeft +"px";
    underline.style.width = e.currentTarget.offsetWidth = "px";
    underline.style.top = e.currentTarget.offsetTop + e.currentTarget.offsetHeight + "px";
}

/* 이미지 옮기기! */

