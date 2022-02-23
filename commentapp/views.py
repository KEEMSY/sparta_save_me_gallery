import random
import json
from django.core.paginator import Page, Paginator
from django.http import HttpResponse
from django.shortcuts import render
from commentapp.models import Comment
from random import randrange
# Create your views here.


def get_comment_page(request)-> Page:
    if request.method == 'GET':
        comment_list = Comment.objects.order_by('-created_at').all() #생성시간 역순으로 모두불러오기
        paginator = Paginator(comment_list, 3) #댓글리스트를 한 페이지에 3개씩 불러오는 페이지네이터 정의
        page = request.GET.get('page') #html에서 페이지 불러서 페이지로 넘겨주기(a태그의 href="?page={{}}에서 받아옴)
        comments = paginator.get_page(page)#현재 페이지에 표시될 댓글들을 넘겨줌
        return render(request, 'commentapp/comment_test.html', {'comments':comments})
    else:
        a = random.randrange(1,6)
        profile_img = "static/img/f'{a}.jpg'"
        Comment.objects.create( #생성시 알아서 저장.
            username=request.POST['username'],
            password = request.POST['password'],
            comment = request.POST['comment'],
        )
        context = {
            'profile_img': profile_img,
            'msg':'Successfully saved!'
        }
        return HttpResponse(json.dumps(context), content_type='application/json')

