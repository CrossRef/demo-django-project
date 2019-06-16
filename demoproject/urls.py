from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("critter", views.critter, name="critter"),
    # Naive...
    path("naive/numbers", views.naive_numbers),
    path("naive/numbers/<int:num_id>", views.naive_number),
    # Using REST API
    url(r"^", include(views.numbers_router.urls)),
    url(r"^docs/", include_docs_urls(title="My Catalogue of Numbers")),
    # Prometheus
    url("", include("django_prometheus.urls")),
]
