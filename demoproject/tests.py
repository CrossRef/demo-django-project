from django.test import SimpleTestCase
from demoproject import views
import json

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()

class NumbersTestCase(SimpleTestCase):
    def setUp(self):
        pass

    def test_numbers_have_ids(self):
        self.assertEqual(views.NUMBERS[1002]['id'], 1002)


class NumbersAPITestCase(SimpleTestCase):
    def test_all_nums_returned(self):

        # TODO there may be a better way. 
        # https://www.django-rest-framework.org/api-guide/testing/
        view = views.NumberViewSet.as_view({'get': 'list'})
        request = factory.get('/numbers')
        response = view(request)
        response.render()
        body = json.loads(response.content)

        self.assertEqual(len(body), len(views.NUMBERS))
