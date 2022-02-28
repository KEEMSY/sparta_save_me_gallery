import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from commentapp.services.comment_service import get_comment_page, add_comment, delete_comment


def comment_page(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        comments = get_comment_page(page)
        return render(request, 'commentapp/comments.html', {'comments': comments})
    else: #POST요청으로 왔을때
        username = request.POST['username']
        password=request.POST['password']
        comment=request.POST['comment']
        add_comment(username,password,comment)
        context = {'msg': 'Successfully Saved!' }
        return HttpResponse(json.dumps(context), content_type='application/json')


def delete(request):
    print(request.body)
    jsonObject = json.loads(request.body.decode('utf-8'))
    username = jsonObject.get('username')
    password = jsonObject.get('password')
    id = jsonObject.get('id')
    msg = delete_comment(username, password, id)
    return JsonResponse({ 'msg' : msg })








