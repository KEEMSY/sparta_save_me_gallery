from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from activityapp.models import Activity


def upload_activity_page(request):
    if request.method['GET']:
        return render(request, 'templates/activityapp/upload.html')


def save_made_img(request):
    # 데이터가 어떻게 오느냐에따라 수정해야함
    if "intenstion" == "yes":
        Activity.objects.create(
            name="name",
            pwd="pwd",
            img="image_URL",
        )
        return render(request, JsonResponse({'msg': 'Your own masterpiece is successfully saved!'}))
    else:
        return redirect('activityapp:upload')
