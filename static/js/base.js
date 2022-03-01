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

var full_link = document.location.href.split('/');
var develop_url = '/' + full_link[3]


let underline = document.getElementById('under_bar')
let menu_list = document.querySelectorAll('div.nav_context_box a')

menu_list.forEach((menu) =>
    menu.addEventListener('mouseover', (e) => indicator(e)))

menu_list.forEach((menu) =>
    menu.addEventListener('mouseout', (e) => initial_underline()))

function indicator(e) {
    underline.style.left = e.currentTarget.offsetLeft + 15 + "px";
    underline.style.width = e.currentTarget.offsetWidth - 30 + "px";
    underline.style.top = e.currentTarget.offsetTop + e.currentTarget.offsetHeight - 20 + "px";
    underline.style.animation = 'underline_appear 1s ease-in'
}

function initial_underline() {
    underline.style.animation = ''
    if (develop_url === '/') {
        draw_initial_under_line(0)
    } else if (develop_url === '/activities') {
        draw_initial_under_line(1)
    } else if (develop_url === '/comments') {
        draw_initial_under_line(2)
    } else if (develop_url === '/info') {
        draw_initial_under_line(3)
    }


}

function draw_initial_under_line(index) {
    menu_list[index].style.color = '#390D0D'
    menu_list[index].animation = 'underline_appear 1s ease-in'
    underline.style.left = menu_list[index].offsetLeft + 15 + "px";
    underline.style.width = menu_list[index].offsetWidth - 30 + "px";
    underline.style.top = menu_list[index].offsetTop + menu_list[index].offsetHeight - 20 + "px";

}




/* 이미지 옮기기! */

/* 위로 옮기기! */

function move_to_top(){
    window.scrollTo(0, 0)
}