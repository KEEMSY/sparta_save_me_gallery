from django.core.paginator import Page, Paginator

from activityapp.models import Activity


def get_activity_page(page: int, limit: int) -> Page:
    return Paginator(Activity.objects.order_by("-id"), limit).page(page)
