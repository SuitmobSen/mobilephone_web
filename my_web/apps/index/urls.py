from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^search/", views.search, name="search"),
    url(r"^about/$", views.about, name="about"),
    url(r'^$', views.index, name="index"),
]