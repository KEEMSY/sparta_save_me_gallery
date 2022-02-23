from django.core.paginator import Page, Paginator

from activityapp.models import Activity


def get_activity_page(page: int, limit: int) -> Page:
    return Paginator(Activity.objects.order_by("-id"), limit).page(page)


def create_Activity(name:str,pwd:str,img:str) -> Activity:
    return Activity.objects.create(name=name, password=pwd, img=img)