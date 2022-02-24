import random
import json
from django.core.paginator import Page, Paginator
from django.http import HttpResponse
from django.shortcuts import render
from commentapp.models import Comment


# Create your views here.
from commentapp.services.comment_service import get_comment_page, add_comment


def comment_page(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        comments = get_comment_page(page)
        return render(request, 'commentapp/comment_test.html', {'comments': comments})
    else:
        username = request.POST['username']
        password=request.POST['password']
        comment=request.POST['comment']
        new_comment = add_comment(username,password,comment)
        context = {'msg': 'Successfully saved!'}
        return HttpResponse(json.dumps(context), content_type='application/json')



#     if request.method == 'GET':
#
#         comment_list = Comment.objects.order_by('-created_at').all()  # 생성시간 역순으로 모두불러오기
#         paginator = Paginator(comment_list, 3)  # 댓글리스트를 한 페이지에 3개씩 불러오는 페이지네이터 정의
#         page = request.GET.get('page')  # html에서 페이지 불러서 페이지로 넘겨주기(a태그의 href="?page={{}}에서 받아옴)
#         comments = paginator.get_page(page)  # 현재 페이지에 표시될 댓글들을 넘겨줌
#         return render(request, 'commentapp/comment_test.html', {'comments': comments})
#         # 여기서 else를 get요청이아닌 다른 방식으로 들어왔을때 에러메세지 띄워주...?
#     else:  # ajax로 댓글작성요청이 들어오면 함수따로작성해야하나요...? /comment/add, def add_comment(request)
#         profile_img = "/static/img/" + str(random.randrange(1, 6)) + ".jpg"
#         Comment.objects.create(  # 생성시 알아서 저장.
#             username=request.POST['username'],
#             password=request.POST['password'],
#             comment=request.POST['comment'],  # 댓글모델에 profile_img를 저장해야 해당이미지를 이댓글이 계속 가져가지 않을까요?
#         )
#         context = {
#             'profile_img': profile_img,
#             'msg': 'Successfully saved!'
#         }
#         return HttpResponse(json.dumps(context), content_type='application/json')
#
#
# def delete_comment(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     comment = request.POST['comment']
#     # 아예 내용까지 받아서 삭제할 수 있도록 하는건 어떨지?
#     found_comment = Comment.objects.filter(username=username, comment=comment)
#     # 유저이름과 댓글내용 일치하는 댓글을 찾아서 found_comment에 담음
#     if found_comment:  # found_comment가 있으면.. (근데 작성자, 비밀번호가 같은글이 여러개면?)
#         if password == found_comment.password:
#             found_comment.delete()
#             context = {'msg': 'Successfully deleted'}
#             return HttpResponse(json.dumps(context), content_type='application/json')
#         else:  # 비밀번호가 일치하지 않는다면
#             return JsonResponse({'msg': 'incorrect password'})
#     else:  # found_comment가 없다면?
#         return JsonResponse({'msg': 'Wrong approach'})