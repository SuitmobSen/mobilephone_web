from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r"^$", views.News.as_view(), name="news"),
    url(r'^(?P<id>\d+)/$', views.NewsDetail.as_view(), name="news_detail"),
]