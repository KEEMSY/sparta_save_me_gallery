from django.core.exceptions import MultipleObjectsReturned
from django.test import TestCase

from activityapp.models import Activity
from activityapp.services.activity_service import (create_Activity,
                                                   get_activity_page_load)

# Given
# When
# Then
# expect


class TestView(TestCase):
    def test_get_activity_page(self) -> None:
        # Given
        activities = [Activity.objects.create(name=f"{i}") for i in range(1, 21)]

        # When
        result_activities = get_activity_page_load(1)

        # Then
        self.assertEqual(len(result_activities), 6)
        self.assertEqual("20", result_activities[0].name)

    # objects.get()값이 여러개가 반환 될경우 에러발생
    def test_create_Activity(self):
        # Given
        user1 = create_Activity(123, 1234, 1)
        user2 = create_Activity(123, 123, 2)

        # Expect
        with self.assertRaises(MultipleObjectsReturned):
            result1 = Activity.objects.get(name=123)

    # 최신 게시물로 업로드
    def test_activity_page_load(self):
        # Given
        page = 1
        # activity 객체 20개 생성
        activity_list = [create_Activity(i, 123, 123) for i in range(21)]
        load_page = get_activity_page_load(page)
        print(load_page)

        # When
        add_activity_list = [create_Activity(i, 123, 123) for i in range(21, 41)]

        # expect
        next_load_page = get_activity_page_load(page)
        print(next_load_page)
