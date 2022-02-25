import json
from django.http import JsonResponse
from django.shortcuts import render
from commentapp.services.comment_service import get_comment_page, add_comment, delete_comment

# Create your views here.



def comment_page(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        comments = get_comment_page(page)
        return render(request, 'commentapp/comment_test.html', {'comments': comments})
    else: #POST요청으로 왔을때
        jsonObject = json.loads(request.body.decode('utf-8'))
        username = jsonObject.get('username')
        password=jsonObject.get('password')
        comment=jsonObject.get('comment')
        add_comment(username,password,comment)
        return JsonResponse({'msg': 'Successfully Saved!'})


def delete(request):
    jsonObject = json.loads(request.body.decode('utf-8'))
    username = jsonObject.get('username')
    password = jsonObject.get('password')
    comment = jsonObject.get('comment')
    msg = delete_comment(username, password, comment)
    return JsonResponse({ 'msg' : msg })









