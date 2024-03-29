from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 登录
    url(r"^login/$", views.Login.as_view(), name="login"),
    # 注册
    url(r"^reg/$", views.Register.as_view(), name="register"),
    # 退出
    url(r'^logout/$', views.logout, name="logout"),
    # 个人中心
    # url(r"^center/$", views.center, name="center"),
    # 个人资料
    url(r'^center/profile/$', views.ProfileView.as_view(), name='profile'),
    # 修改密码
    url(r'^center/change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),
    # 忘记密码
    url(r'password/forget/$', views.PasswordForget.as_view(), name="password_forget"),
    # 密码重置
    url(r'password/reset/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),
]
