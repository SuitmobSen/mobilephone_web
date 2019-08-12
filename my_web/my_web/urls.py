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

    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    # 主页
    url(r"^", include("apps.index.urls", namespace="index")),
]

