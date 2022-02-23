from django.test import TestCase

from activityapp.models import Activity
from activityapp.services.activity_service import get_activity_page


class TesView(TestCase):

    def test_get_activity_page(self) -> None:
        # Given
        activities = [Activity.objects.create(name=f'{i}') for i in range(1, 21)]

        # When
        result_activities = get_activity_page(1, 6)

        # Then
        self.assertEqual(len(result_activities), 6)
        self.assertEqual('20', result_activities[0].name)

