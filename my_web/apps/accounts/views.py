from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
import logging
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .forms import RegisterForm, LoginForm, FindpasswdForm, ResetpasswdForm
from .models import FindPassword
from .models import User
from django.core.mail import send_mail
import random
import string
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


class PasswordForget(View):
    def get(self, request):
        form = FindpasswdForm()
        return render(request, "accounts/password_forget.html", {"form": form})

    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            form = FindpasswdForm(request.POST)
            if form.is_valid():
                email = form.clean_email()
                verify_code = "".join(random.choices(string.ascii_lowercase+string.digits, k=128))
                url = f"{request.scheme}://{request.META['HTTP_HOST']}/accounts/password/reset/{verify_code}?email={email}"
                ret = FindPassword.objects.get_or_create(email=email)
                # (<FindPassword: FindPassword object>, True)
                ret[0].verify_code = verify_code
                ret[0].status = False
                ret[0].save()
                print(url)
                print("发邮件")
                send_mail('重置密码验证信息', url, None, [email])
                ret["status"] = 200
                ret["msg"] = "邮件发送成功，请登录邮箱查看！"
                return JsonResponse(ret)
            else:
                ret["status"] = 404
                ret["msg"] = "输入的邮箱不存在！"
        logger.debug(f"邮箱验证结果：{ret}")
        return JsonResponse(ret)


class PasswordReset(View):
    def get(self, request, verify_code):
        form = ResetpasswdForm()
        import datetime
        create_time_newer = datetime.datetime.utcnow()-datetime.timedelta(minutes=30)
        email = request.GET.get("email")
        print(email)
        # 邮箱、verify_code、status=False、时间近30分钟
        find_password = FindPassword.objects.filter(status=False, verify_code=verify_code, email=email, creat_time__gte=create_time_newer)
        # great_then_equal, lte, lt, gt
        if verify_code and find_password:
            return render(request, "accounts/password_reset.html", {"form": form})
        else:
            return HttpResponse("此链接已失效")

    def post(self, request, verify_code):
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax:
            form = ResetpasswdForm(request.POST)
            if form.is_valid():
                print("合法")
                import datetime
                create_time_newer = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
                password1 = form.cleaned_data.get("password1")
                password2 = form.cleaned_data.get("password2")
                if password2 == password1:
                    try:
                        find_password = FindPassword.objects.get(status=False, verify_code=verify_code, creat_time__gte=create_time_newer)
                        user = User.objects.get(email=find_password.email)
                        user.set_password(password1)
                        user.save()
                        ret = {"status": 200, "msg": "密码已重置，请登录"}
                        find_password.status = True
                        find_password.save()
                    except Exception as ex:
                        logger.debug(ex)
                        ret = {"status": 401, "msg": "出错了..."}
                else:
                    ret['status'] = 402
                    ret["msg"] = "两次密码不一致"
        return JsonResponse(ret)


def center(request):
    pass