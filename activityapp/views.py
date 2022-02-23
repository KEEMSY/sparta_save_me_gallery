from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from activityapp.models import Activity
from activityapp.services.activity_service import get_activity_page

limit = 6


def upload_activity_page(request, offset):
    if request.method['GET']:
        return render(request, 'templates/activityapp/upload.html', JsonResponse({get_activity_page(0, limit)}))
    else:
        return render(request, 'templates/activityapp/upload.html', JsonResponse({get_activity_page(offset, limit)}))


def save_made_img(request):
    # 데이터가 어떻게 오느냐에따라 수정해야함
    if "intenstion" == "yes":
        Activity.objects.create(
            name=request.POST.get("name", ''),
            pwd=request.POST.get("pwd", ''),
            img=request.POST.get("image_URL", ''),
        )
        return render(request, JsonResponse({'msg': 'Your own masterpiece is successfully saved!'}))
    else:
        return redirect('activityapp:upload')
