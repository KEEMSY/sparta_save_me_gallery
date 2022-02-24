import random
import json
from django.core.paginator import Page, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from commentapp.models import Comment


def get_comment_page(page:int)-> Page:
    comment_list = Comment.objects.order_by('-created_at').all() #생성시간 역순으로 모두불러오기
    paginator = Paginator(comment_list, 3) #댓글리스트를 한 페이지에 3개씩 불러오는 페이지네이터 정의
    comments = paginator.get_page(page)#현재 페이지에 표시될 댓글들을 넘겨줌
    return comments

def add_comment(username:str, password:str, comment:str):
    profile_img = "/static/img/"+str(random.randrange(1,6))+".jpg"
    new_comment = Comment.objects.create(
        username=username,
        password = password,
        comment=comment,
        profile_img=profile_img)
    #댓글모델에 profile_img를 저장해야 해당이미지를 이댓글이 계속 가져가지 않을까요?
    return new_comment

def delete_comment(password):


    #아예 내용까지 받아서 삭제할 수 있도록 하는건 어떨지?
    found_comment = Comment.objects.filter(username=username, comment=comment).get()
    #유저이름과 댓글내용 일치하는 댓글을 찾아서 found_comment에 담음
    if found_comment: #found_comment가 있으면.. (근데 작성자, 비밀번호가 같은글이 여러개면?)
        if password == found_comment.password:
            found_comment.delete()
            context = {'msg':'Successfully deleted'}
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:#비밀번호가 일치하지 않는다면
            return JsonResponse({'msg':'incorrect password'})
    else:# found_comment가 없다면?
        return JsonResponse({'msg': 'Wrong approach'})





