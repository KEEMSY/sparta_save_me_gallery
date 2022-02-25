from django.core.exceptions import MultipleObjectsReturned
from django.test import TestCase

from activityapp.models import Activity
from activityapp.services.activity_service import (get_activity_page_load, create_activity, load_activity, )

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
        user1 = create_activity(1, 123, 1234, 1)
        user2 = create_activity(1, 123, 123, 2)

        # Expect
        with self.assertRaises(MultipleObjectsReturned):
            result1 = Activity.objects.get(name=123)

    # 최신 게시물로 업로드
    def test_activity_page_load(self):
        # Given
        page = 1
        # activity 객체 20개 생성
        activity_list = [create_activity(1, i, 123, 123) for i in range(21)]
        load_page = get_activity_page_load(page)
        print(load_page)

        # When
        add_activity_list = [create_activity(1, i, 123, 123) for i in range(21, 41)]

        # expect
        next_load_page = get_activity_page_load(page)
        print(next_load_page)

    # 모델 종류 별 게시물 불러오기
    def test_load_all_of_activities(self):
        # Given
        # 종류(3) 별로 5개씩 만듬
        activity_list = [[create_activity(i, j, 123, 123) for i in range(3)]for j in range(20,25)]

        # When
        all_activities = []
        for i in range(3):
            all_activities.append(load_activity(i))

        # Then
        for actitivy in all_activities:
            print('activity',actitivy)
            for one in actitivy:
                print("model_name",one.model_name)
                print("name",one.name)

        print('all_activities',all_activities)

    def test_load_latest_activities_upto_20(self):
        # Given
        # 종류(3) 별로 5개씩 만듬
        activity_list = [[create_activity(i, j, 123, 123) for i in range(3)] for j in range(21, 50)]

        all_activities = []
        for i in range(3):
            all_activities.append(load_activity(i))

        for actitivy in all_activities:
            print('activity',actitivy)
            for one in actitivy:
                print("model_name",one.model_name)
                print("name",one.name)
        # When
        new_activity_list = [[create_activity(a, b, 123, 123) for a in range(3)] for b in range(50, 100)]
        print(("@@@@@  after  @@@@@"))


        # Then
        new_all_activities = []
        for i in range(3):
            new_all_activities.append(load_activity(i))

        for actitivy in new_all_activities:
            print('activity', actitivy)
            for one in actitivy:
                print("model_name", one.model_name)
                print("name", one.name)