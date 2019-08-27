"""my_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.views.static import serve
import re
from . import settings
from .settings import MEDIA_ROOT
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 日志
    url(r'^logtest/$', views.logtest, name="logtest"),
    # 账户
    url(r"^accounts/", include("apps.accounts.urls", namespace="accounts")),
    # 所有手机信息模块
    url(r"^info/", include("apps.info.urls", namespace="phone_info")),
    # 所有测评视频模块
    url(r"^videos/", include("apps.videos.urls", namespace="phone_videos")),
    # 所有数码新闻模块
    url(r"^news/", include("apps.news.urls", namespace="phone_news")),
    # 接口
    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    # meida 处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 主页
    url(r"^", include("apps.index.urls", namespace="index")),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,
        {"document_root": settings.STATIC_ROOT}),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, {"document_root": settings.MEDIA_ROOT}),
]

handler404 = views.my404

