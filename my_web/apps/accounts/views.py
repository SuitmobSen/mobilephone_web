from django.shortcuts import render, redirect, reverse
from django.views.generic import View
import logging
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .forms import RegisterForm, LoginForm
from .models import User
# Create your views here.

logger = logging.getLogger('accounts')


class Login(View):
    # 当加载Login页面时
    def get(self, request):
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        if request.user.is_authenticated:
            return redirect(reverse('index:index'))
        form = LoginForm()
        # 设置下一跳转地址
        request.session["next"] = request.GET.get('next', reverse('index:index'))
        return render(request, "accounts/login.html", {"form": form})

    # Form表单直接提交
    def post(self, request):
        # 表单数据绑定
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data["mobile"]
            captcha = form.cleaned_data["captcha"]
            session_captcha_code = request.session.get("captcha", "")
            logger.debug(f"登录提交验证码:{captcha}-{session_captcha_code}")
            # 验证码一致
            if captcha.lower() == session_captcha_code.lower():
                user, flag = form.check_password()
                if flag and user and user.is_active:
                    auth.login(request, user)
                    logger.info(f"{user.mobile}登录成功")
                    # 跳转到next
                    return redirect(request.session.get("next", '/'))
                msg = "用户名或密码错误"
                logger.error(f"用户{mobile}登录失败, 用户名或密码错误")
            else:
                msg = "验证码错误"
                logger.error(f"用户{mobile}登录失败, 验证码错误")
        else:
            msg = "无效的信息"
            logger.error(msg)
        return render(request, "accounts/login.html", {"form": form, "msg": msg})


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                mobile = form.cleaned_data["mobile"]
                password = form.cleaned_data["password"]
                # mobile = form.cleaned_data["mobile"]
                # mobile_captcha = form.cleaned_data["mobile_captcha"]
                # mobile_captcha_reids = cache.get(mobile)
                # if mobile_captcha == mobile_captcha_reids:
                user = User.objects.create(username=mobile, mobile=mobile, password=make_password(password))
                user.save()
                ret['status'] = 200
                ret['msg'] = f"新用户{user}注册成功！"
                logger.debug(f"新用户{user}注册成功！")
                user = auth.authenticate(username=mobile, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    logger.debug(f"新用户{user}登录成功")
                else:
                    logger.error(f"新用户{user}登录失败")
                # else:
                #     # 验证码错误
                #     ret['status'] = 401
                #     ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
        logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)


def logout(request):
    auth.logout(request)
    return redirect(reverse("index:index"))


def center(request):
    pass
