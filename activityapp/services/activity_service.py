from django.core.paginator import Page, Paginator

from activityapp.models import Activity


def get_activity_page_load(page: int) -> Activity:
    # 6개씩 보여짐
    limit = 6
    offset = limit * (page - 1)
    activity_list = Activity.objects.order_by("-id")[offset: offset + limit]
    return activity_list


def create_activity(model_name: str, name: str, pwd: str, img: str) -> Activity:
    return Activity.objects.create(model_name=model_name, name=name, password=pwd, img=img)


def activity_pagenator(page: int) -> Page:
    activity_list = Activity.objects.order_by("-id")
    paginator = Paginator(activity_list, 3)
    posts = paginator.get_page(page)
    return posts


def activity_load(name):
    model = Activity.objects.order_by('-id').filter(model_name=name)
    return model
