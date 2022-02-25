import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from activityapp.models import Activity
from activityapp.services.activity_service import (create_activity,
                                                   get_activity_page_load, activity_load)


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
def upload_activity_page(request):
    all_activities = []
    # 해당 모델이름들을 담아둬여함
    models = []
    for model in models:
        all_activities.append(activity_load(model))

    return render(request, "activityapp/upload.html", {"all_activities":all_activities})


# POST인경우만 존재
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
        return redirect("activityapp:upload")
