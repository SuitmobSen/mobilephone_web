from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r"^login/$", views.Login.as_view(), name="login"),
    url(r"^reg/$", views.Register.as_view(), name="register"),
    # 退出
    url(r'logout/$', views.logout, name="logout"),
    url(r"^center/$", views.center, name="center"),
]
