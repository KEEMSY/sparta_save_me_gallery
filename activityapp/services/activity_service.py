from django.core.paginator import Page, Paginator

from activityapp.models import Activity


def get_activity_page_load(page: int) -> Activity:
    # 6개씩 보여짐
    limit = 6
    offset = limit * (page - 1)
    activity_list = Activity.objects.order_by("-id")[offset : offset + limit]
    return activity_list


def create_Activity(name: str, pwd: str, img: str) -> Activity:
    return Activity.objects.create(name=name, password=pwd, img=img)


def activity_pagenator(page: int) -> Page:

    activity_list = Activity.objects.order_by("-id")
    paginator = Paginator(activity_list, 3)
    posts = paginator.get_page(page)
    return posts
