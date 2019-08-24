from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r"^phones/$", views.phones, name="phones"),
    url(r"^phones/(?P<id>\d+)/phone_list/$", views.phone_list, name="phone_list"),
    url(r"^phones/(?P<id>\d+)/phone_list/(?P<phoneid>\d+)$", views.phone_detail, name="phone_detail"),
    url(r"^phones/(?P<id>\d+)/phone_list/(?P<phoneid>\d+)/more_params/$", views.more_params, name="more_params")
]
