import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from commentapp.services.comment_service import get_comment_page, add_comment, delete_comment


def comment_page(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        comments = get_comment_page(page)
        return render(request, 'commentapp/comment_test.html', {'comments': comments})
    else: #POST요청으로 왔을때
        username = request.POST['username']
        password=request.POST['password']
        comment=request.POST['comment']
        add_comment(username,password,comment)
        return JsonResponse({'msg': 'Successfully Saved!'})


def delete(request):
    username = request.POST['username']
    password = request.POST['password']
    comment = request.POST['comment']
    msg = delete_comment(username, password, comment)
    return JsonResponse({ 'msg' : msg })









