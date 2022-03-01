

$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    initial_underline()
});

function appear(id) {
    let target = document.getElementById(id)
    let modal = target.children[0]
    modal.style.display = 'flex'
    target.style.transform = 'scale(1.1)'
    target.style.zIndex = '2'
}

function disappear(id) {
    let target = document.getElementById(id)
    let modal = target.children[0]
    modal.style.display = 'none'
    target.style.transform = 'scale(1)'
    target.style.zIndex = '0'
}


function move_to_upload() {
    window.scrollTo(0, 1300)

    window.addEventListener('scroll', function () {
        let value = window.scrollY
        console.log(value)
    })
}

window.addEventListener('scroll', function () {
    let value = window.scrollY

    let up_box = document.getElementById('up_button')
    if(value >= 100){
        up_box.style.display = 'block'
    }
    else{
        up_box.style.display = 'none'
    }
})

function upload_image() {
    let img = document.getElementById('upload_file').files[0];
    let preview_img = document.getElementById('preview_image');
    const file_url = URL.createObjectURL(img);
    preview_img.style.backgroundImage = `url(${file_url})`
    preview_img.style.backgroundColor = 'white'
    setTimeout(function () {
        // scroll_to(2464)
        window.scrollTo(0, 2464)
    }, 1000);

    // console.log(img)
    // console.log(file_url)

    // let reader = new FileReader();
    // reader.readAsDataURL(img);
    // preview_img.style.backgroundImage = `url('${reader.result}')`;
    // console.log(reader);


}

function scroll_to(target_scroll) {
    let current_scroll = window.scrollY

    let gap = target_scroll - current_scroll


    while (gap >= 0) {
        gap -= 10
        current_scroll += 10

        setTimeout(function () {
            window.scrollTo(0, current_scroll)

        }, 100);

    }
}


var swiper = new Swiper(".select_box", {
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});




function test(index) {
    swiper.slideTo(index)
}

let underline_2 = document.getElementById('select_style')
let select_list = document.querySelectorAll('div.select_style_name ')

select_list.forEach((menu)=>
    menu.addEventListener('click',(e)=> draw_select_style(e)))


function draw_select_style(e){
    underline_2.style.left = e.currentTarget.offsetLeft + "px";
    underline_2.style.width = e.currentTarget.offsetWidth + "px";
    underline_2.style.top = 10 + e.currentTarget.offsetTop + e.currentTarget.offsetHeight + "px";
}

function covert_img() {

    let model_type = document.getElementById('style_' + swiper.realIndex).innerText
    let image = $('#upload_file')[0].files[0]
    let image_name = image['name'].split('.')[0]
    let form_data = new FormData()


    form_data.append("image_name", image_name)
    form_data.append("model_type", model_type)
    form_data.append("image", image)

    console.log(form_data)
    $.ajax({
        type: "POST",
        url: "http://localhost:5000/api/convert/",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log('response data : ', response)
            console.log(response['stylized_img_url'])
            document.getElementById('result_img').src = response['stylized_img_url']
        }
    });


    let painting_div = document.getElementById('painting')
    painting_div.innerText = model_type
    window.scrollTo(0, 3764)
}

function open_save_box() {
    let radio_box = document.getElementById('save_box')
    let radio_check = document.getElementsByClassName('radio_fill')
    radio_check[0].style.display = 'block'
    radio_check[1].style.display = 'none'
    console.log(radio_box)
    radio_box.style.display = 'block'
}

function close_save_box() {
    let radio_box = document.getElementById('save_box')
    let radio_check = document.getElementsByClassName('radio_fill')
    document.getElementById('name').value = ''
    document.getElementById('password').value = ''

    radio_check[0].style.display = 'none'
    radio_check[1].style.display = 'block'
    radio_box.style.display = 'none'
}

function save_result_img() {
    let name = document.getElementById('name').value
    let pwd = document.getElementById('password').value
    let model_name = document.getElementById('painting').innerText
    let mage_URL = document.getElementById('result_img').src


    $.ajax({
        type: 'post',
        url: '/activities/image/',
        data: {
            'intention': '',
            'name':name,
            'password': pwd,
            'model_name': model_name,
            'made_image': mage_URL
        },
        success: function(response){
            alert('saved!')
            console.log(response['msg'])
        }
    })
    close_save_box()
    window.location.href='/'
}