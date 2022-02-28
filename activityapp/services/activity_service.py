from django.core.paginator import Page, Paginator

from activityapp.models import Activity, Info


def get_activity_page_load(page: int) -> Activity:
    # 6개씩 보여짐
    limit = 6
    offset = limit * (page - 1)
    activity_list = Activity.objects.order_by("-id")[offset: offset + limit]
    return activity_list


def create_activity(model_name: str, name: str, pwd: int, img: str) -> Activity:
    return Activity.objects.create(model_name=model_name, name=name, password=pwd, img=img)


def delete_activity(pk, password) -> dict:
    target_activity = Activity.objects.get(pk=pk)
    if target_activity.password == str(password):
        target_activity.delete()
        return {'msg': 'success'}
    else:
        return {'msg': 'fail'}


# 최신순 최대 20개까지 가옴옴
def load_activity(name):
    model = Activity.objects.order_by('-id').filter(model_name=name)[:20]
    return model


def create_info(model_name: str, model_img: str, example_img: str):
    return Info.objects.create(model_name, model_img=model_img, example_img=example_img)
