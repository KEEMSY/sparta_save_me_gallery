import random
from django.core.paginator import Page, Paginator
from commentapp.models import Comment


def get_comment_page(page:int)-> Page:
    comment_list = Comment.objects.order_by('-created_at').all() #생성시간 역순으로 모두불러오기
    paginator = Paginator(comment_list, 3) #댓글리스트를 한 페이지에 3개씩 불러오는 페이지네이터 정의
    comments = paginator.get_page(page)#현재 페이지에 표시될 댓글들을 넘겨줌
    return comments

def add_comment(username:str, password:str, comment:str) -> Comment:
    profile_img = "/static/img/"+str(random.randrange(1,6))+".jpg"
    return Comment.objects.create(username=username,password = password,comment=comment,profile_img=profile_img)

def delete_comment(password:str, id:str):
    #작성자명과, 댓글내용으로 해당 댓글객체를 가져와서
    found_comment = Comment.objects.filter(pk=id).get()
    #유저이름과 댓글내용 일치하는 댓글을 찾아서 found_comment에 담음
    if found_comment: #found_comment가 있으면..
        if password == found_comment.password:
            found_comment.delete()
            msg = 'Successfully deleted'
            return msg
        else:#비밀번호가 일치하지 않는다면
            msg = 'Incorrect password'
            return msg
    else:# found_comment가 없다면?
        msg = 'Wrong approach'
        return msg





