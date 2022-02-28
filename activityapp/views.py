import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from activityapp.models import Activity, Info
from activityapp.services.activity_service import (create_activity,
                                                   get_activity_page_load, load_activity)


# 페이지에는 최신의 6개의 activity가 보여짐
def home(request):
    if request.method == "GET":
        return render(
            request, "index.html", {"activities": get_activity_page_load(1)}
        )
    else:
        return JsonResponse({"activities": get_activity_page_load(1)})


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
def save_made_img(request):
    jsonObject = json.loads(request.body.decode('utf-8'))
    if jsonObject.get("intenstion") == "yes":
        create_activity(
            jsonObject.get("model_name"),
            jsonObject.get("name"),
            jsonObject.get("pwd"),
            jsonObject.get("image_URL")
        )
        return JsonResponse({"msg": "Your own masterpiece is successfully saved!"})
    else:
        return redirect("activityapp:choice")
