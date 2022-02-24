from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from activityapp.models import Activity
from activityapp.services.activity_service import  get_activity_page_load ,create_Activity



def home(request):
    if request.method == 'GET':
        return render(request, 'templates/activityapp/test_index.html',get_activity_page_load(0))
    else:
        page = request.POST.get('page')
        return JsonResponse({'activities': get_activity_page_load(page)})


def upload_activity_page(request, offset):
    return render(request, 'templates/activityapp/upload.html')



# POST인경우만 존재
def save_made_img(request):
    # 데이터가 어떻게 오느냐에따라 수정해야함
    if "intenstion" == "yes":
        create_Activity(request.POST.get("name", ''),
                        request.POST.get("pwd", ''),
                        request.POST.get("image_URL", ''))

        return JsonResponse({'msg': 'Your own masterpiece is successfully saved!'})
    else:
        return redirect('activityapp:upload')
