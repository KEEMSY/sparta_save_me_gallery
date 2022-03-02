

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

// window.addEventListener('scroll', function () {
//         let value = window.scrollY
//         console.log(value)
//     })

function move_to_upload() {
    window.scrollTo(0, 990)
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


function open_tip_box(){
    let modal_box = document.getElementById('modal_tip')
    if(modal_box.style.display==='block'){
        modal_box.style.display = 'none'
        window.scrollTo(0, 990)
    }
    else{
        modal_box.style.display = 'block'
        window.scrollTo(0, 434)
    }

}


function upload_origin_image(){
    let img = document.getElementById('upload_origin_file').files[0];
    let preview_img = document.getElementById('preview_image_origin');
    const file_url = URL.createObjectURL(img);
    preview_img.style.backgroundImage = `url(${file_url})`
    preview_img.style.backgroundColor = 'white'
}

function upload_style_image(){
    let img = document.getElementById('upload_style_file').files[0];
    let preview_img = document.getElementById('preview_image_style');
    const file_url = URL.createObjectURL(img);
    preview_img.style.backgroundImage = `url(${file_url})`
    preview_img.style.backgroundColor = 'white'
}


function covert_custom_img(){
    let image = $('#upload_origin_file')[0].files[0]
    let model_image = $('#upload_style_file')[0].files[0]

    console.log(image)
    console.log(model_image)

    if(image === undefined  || model_image === undefined ){
        window.scrollTo(0, 990)
        return alert('Upload your photo!')
    }


    let image_name = image['name'].split('.')[0]
    let model_image_name = 'others'


    let form_data = new FormData()

    form_data.append("image_name", image_name)
    form_data.append("image", image)
    form_data.append("model_image_name", model_image_name)
    form_data.append("model_image", model_image)

    // 인공 지능 서버 연결
    $.ajax({
        type: "POST",
        url: "http://15.165.45.152:5000//api/mix/",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            console.log(response)
            console.log(response['mixed_img_url'])
            document.getElementById('result_custom_img').src = response['mixed_img_url']
        }
    });



    window.scrollTo(0, 2200)
}

function model_2_open_save_box(){
    let radio_box = document.getElementById('model_2_save_box')
    let radio_check = document.getElementsByClassName('model_2_radio_fill')
    radio_check[0].style.display = 'block'
    radio_check[1].style.display = 'none'
    radio_box.style.display = 'block'
}

function model_2_close_save_box(){
    let radio_box = document.getElementById('model_2_save_box')
    let radio_check = document.getElementsByClassName('model_2_radio_fill')
    document.getElementById('model2_name').value = ''
    document.getElementById('model2_password').value = ''

    radio_check[0].style.display = 'none'
    radio_check[1].style.display = 'block'
    radio_box.style.display = 'none'
}

function save_result_custom_img() {
    let name = document.getElementById('model2_name').value
    let password = document.getElementById('model2_password').value
    let mage_URL = document.getElementById('result_custom_img').src
    let model_name = 'default'

    if(mage_URL===''){
        alert('click the Covert button!')
    }

    $.ajax({
        type: 'post',
        url: '/activities/image/',
        data: {
            'name':name,
            'password': password,
            'model_name': 'others',
            'made_image': mage_URL
        },
        success: function(response){
            console.log(response['msg'])
        }
    })

    model_2_close_save_box()
    window.location.href='/'
}