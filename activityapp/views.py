import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from activityapp.models import Activity, Info
from activityapp.services.activity_service import (create_activity,
                                                   get_activity_page_load, load_activity, delete_activity)


# 페이지에는 최신의 6개의 activity가 보여짐
@csrf_exempt
def home(request):
    if request.method == "GET":
        return render(
            request, "index.html", {"activities": get_activity_page_load(1)}
        )
    # 삭제하는 경우
    else:
        # 삭제하는 함수
        msg = delete_activity(request.POST['id'], request.POST['password'])
        if msg['msg'] == "success":
            return JsonResponse({'msg': 'Successfully deleted!'})
        # 이 후 home으로 재연결 해야함
        else:
            return JsonResponse({'msg': 'Passwords do not match!'})


# info페이지
def info(request):
    return render(request, "info.html")


# 업로드 페이지
def choice_activity_page(request):
    all_activities = []
    models = ['la_muse', 'composition', 'starry_night', 'the_wave', 'candy', 'feathers',
              'mosaic', 'the_scream', 'udnie', 'others']
    for model in models:
        all_activities.append(load_activity(model))
    return render(request, "activityapp/choice.html", {"all_activities": all_activities})


# 1: 화풍을 선택 할 경우
def a_choice_activity_page(request):
    return render(request, "activityapp/model1.html", {'all_kind_of_activities': Info.objects.all()})


# 2: 이미지 화풀을 선택 할 경우
def b_choice_activity_page(request):
    return render(request, "activityapp/model2.html")


# 이미지를 저장
@csrf_exempt
def save_made_img(request):
    if 'success' == create_activity(
        request.POST.get("model_name"),
        request.POST.get("name"),
        request.POST.get("password"),
        request.POST.get("made_image")
    ):
        return JsonResponse({"msg": "Your own masterpiece is successfully saved!"})
    else:
        return JsonResponse({'msg': 'Please check the blank'})

