from django.test import SimpleTestCase
from demoproject import views
import json

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


class NumbersTestCase(SimpleTestCase):
    def setUp(self):
        pass

    def test_numbers_have_ids(self):
        self.assertEqual(views.NUMBERS[1002]["id"], 1002)


class NumbersAPITestCase(SimpleTestCase):
    def test_all_nums_returned(self):

        # TODO there may be a better way.
        # https://www.django-rest-framework.org/api-guide/testing/
        view = views.NumberViewSet.as_view({"get": "list"})
        request = factory.get("/numbers")
        response = view(request)
        response.render()
        body = json.loads(response.content)

        self.assertEqual(len(body), len(views.NUMBERS))


class HomePageViewTestCase(SimpleTestCase):
    def test_request_home_page(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello, world.", status_code=200)


class MetricsPageViewTestCase(SimpleTestCase):
    def test_request_home_page(self):
        response = self.client.get("/metrics")
        self.assertEqual(response.status_code, 200)


class MetricsPageCountTestCase(SimpleTestCase):
    def current_home_page_count(self):
        """ extract home page count from /metrics route """
        KEY = 'django_http_requests_latency_seconds_by_view_method_count{method="GET",view="home"}'
        response = self.client.get("/metrics")
        output = response.content.decode()
        parsed = {
            line.split()[0]: line.split()[1]
            for line in output.splitlines()
            if not line.startswith("#")
        }
        return float(parsed[KEY])

    def test_request_home_page(self):
        import random

        number_of_times = random.randint(1, 50)
        start_count = self.current_home_page_count()
        for i in range(number_of_times):
            response = self.client.get("/")
            self.assertTrue(response.status_code == 200)
        end_count = self.current_home_page_count()
        self.assertEqual(start_count + number_of_times, end_count)

