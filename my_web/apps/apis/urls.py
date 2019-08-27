from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 登录图片验证码接口
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    # 上传头像接口
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),
    # 短信验证码接口
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name='mobile_captcha'),
]
