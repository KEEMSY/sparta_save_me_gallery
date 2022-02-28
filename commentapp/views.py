from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from commentapp.services.comment_service import get_comment_page, add_comment, delete_comment

# Create your views here.

@csrf_exempt
def comment_page(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        comments = get_comment_page(page)
        return render(request, 'commentapp/comments.html', {'comments': comments})
    else: #POST요청으로 왔을때
        username = request.POST['username']
        password = request.POST['password']
        comment = request.POST['comment']
        msg = add_comment(username, password, comment)
        return JsonResponse({'msg': msg})

@csrf_exempt
def delete(request):
    username = request.POST['username']
    password = request.POST['password']
    id = request.POST['id']
    msg = delete_comment(username, password, id)
    return JsonResponse({ 'msg' : msg })









