

$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
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
    // console.log(value)
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
    let image_origin = $('#upload_origin_file')[0].files[0]
    let image_style = $('#upload_style_file')[0].files[0]
    let image_name = image['name']
    let form_data = new FormData()

    console.log('model_type', model_type)

    form_data.append("image_name", image_name)
    form_data.append("model_type", model_type)
    form_data.append("image", image)

    console.log(form_data)
    // $.ajax({
    //     type: "POST",
    //     url: "http://localhost:5000/api/convert/",
    //     data: form_data,
    //     cache: false,
    //     contentType: false,
    //     processData: false,
    //     success: function (response) {
    //         console.log(response['stylized_image_url'])
    //         alert(response['stylized_image_url'])
    //     }
    // });

    document.getElementById('result_img').src = 'https://i.pinimg.com/564x/b2/6b/5b/b26b5b036985b8d5b08c4e2d07fcbf04.jpg'

    let painter_div = document.getElementById('painter')
    painter_div.innerText = 'test'
    let painting_div = document.getElementById('painting')
    painting_div.innerText = model_type
    window.scrollTo(0, 3764)
}

function open_save_box(){
    let radio_box = document.getElementById('save_box')
    let radio_check = document.getElementsByClassName('radio_fill')
    radio_check[0].style.display = 'block'
    radio_check[1].style.display = 'none'
    console.log(radio_box)
    radio_box.style.display = 'block'
}

function close_save_box(){
    let radio_box = document.getElementById('save_box')
    let radio_check = document.getElementsByClassName('radio_fill')
    document.getElementById('name').value = ''
    document.getElementById('password').value = ''

    radio_check[0].style.display = 'none'
    radio_check[1].style.display = 'block'
    console.log(radio_box)
    radio_box.style.display = 'none'
}

function save_result_costom_img() {
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
            'pwd': pwd,
            'model_name': model_name,
            'made_image': mage_URL
        },
        success: function(response){
            console.log(response['msg'])
        }
    })

    console.log('name', name)
    console.log('password', pwd)
    console.log('model_type', model_type)
    console.log('result_img', result_img)
}