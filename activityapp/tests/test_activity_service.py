from django.core.exceptions import MultipleObjectsReturned
from django.test import TestCase

from activityapp.models import Activity
from activityapp.services.activity_service import get_activity_page, create_Activity


# Given
# When
# Then
# expect

class TestView(TestCase):

    def test_get_activity_page(self) -> None:
        # Given
        activities = [Activity.objects.create(name=f'{i}') for i in range(1, 21)]

        # When
        result_activities = get_activity_page(1, 6)

        # Then
        self.assertEqual(len(result_activities), 6)
        self.assertEqual('20', result_activities[0].name)

    # objects.get()값이 여러개가 반환 될경우 에러발생
    def test_create_Activity(self):
        # Given
        user1 = create_Activity(123,1234,1)
        user2 = create_Activity(123,123,2)

        # Expect
        with self.assertRaises(MultipleObjectsReturned):
            result1 = Activity.objects.get(name=123)
