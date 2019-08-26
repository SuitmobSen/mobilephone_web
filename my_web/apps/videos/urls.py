from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r"^$", views.Videolist.as_view(), name="videos"),
    # 视频播放页
    url(r'^(?P<id>\d+)/$', views.VideoPlay.as_view(), name="video_play"),
]
