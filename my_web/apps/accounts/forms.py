from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import User, FindPassword
from django.contrib.auth.hashers import check_password as auth_check_password
import re

# 用户注册
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="密 码2",
                                widget=widgets.PasswordInput(attrs={
                                    "id": "password2", "onblur": "check_password2()",
                                    "class": "form-control", "placeholder": "请确认密码", "autocomplete": "off"}))
    mobile_captcha = forms.CharField(label="验证码", max_length=6,
                                     widget=widgets.TextInput(attrs={
                                         "id": "mobile_captcha",
                                         "class": "form-control",
                                         "placeholder": "短信验证码",
                                         "error_messages": {"invalid": "验证码错误"}}))

    class Meta:
        model = User
        fields = ['mobile', 'password']
        widgets = {
            'mobile': widgets.TextInput(
                attrs={"class": "form-control text_phone", "id": "phone",
                       "placeholder": "请输入手机号", "onblur": "check_phone()"}),
            'password': widgets.PasswordInput(
                attrs={"class": "form-control", "id": "password", "autocomplete": "off",
                       "placeholder": "请输入密码", "onblur": "check_password1()"}),
        }

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        re_passwd = re.compile(r"^(?![A-Za-z]+$)(?!\d+$)(?![\W_]+$)\S{6,18}$")
        if not data.isdigit():
            if re.match(re_passwd, data):
                return self.cleaned_data.get("password")
            else:
                raise ValidationError("您设置的密码不符合规则")
        else:
            raise ValidationError("密码不能全是数字")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")


# 登录表单
class LoginForm(forms.Form):
    mobile = forms.CharField(label="用户名", max_length=11,
                             widget=widgets.TextInput(attrs={"class": "form-control",
                                                             "id": "phone",
                                                             "autocomplete": "off",
                                                             "placeholder": "手机号"}))

    password = forms.CharField(label="密 码",
                               widget=widgets.PasswordInput(attrs={"class": "form-control",
                                                                   "id": "password",
                                                                   "autocomplete": "off",
                                                                   "placeholder": "密码"}))
    captcha = forms.CharField(label="验证码", max_length=4,
                              widget=widgets.TextInput(attrs={"class": "form-control text_phone",
                                                              "id": "captcha",
                                                              "placeholder": "验证码",
                                                              "onblur": "check_captcha()",
                                                              "error_messages": {"invalid": "验证码错误"}}))

    def check_password(self):
        print('check password')
        mobile = self.cleaned_data['mobile']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(mobile=mobile)
            return user, auth_check_password(password, user.password)
        except Exception as e:
            print("reason", e)
            return None, False

    def clean_mobile(self):
        print('check mobile')
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号或密码不正确")


class FindpasswdForm(forms.ModelForm):
    class Meta:
        model = FindPassword
        fields = ['email', ]
        widgets = {
            'email': widgets.TextInput(
                attrs={"class": "form-control", "id": "email",
                       "placeholder": "请输入已绑定邮箱", }),
        }

    def clean_email(self):
        ret = User.objects.filter(email=self.cleaned_data.get("email"))
        if ret:
            return self.cleaned_data.get("email")
        else:
            raise ValidationError("您输入的邮箱不存在！")


class ResetpasswdForm(forms.Form):
    password1 = forms.CharField(label="密 码1",
                                widget=widgets.PasswordInput(attrs={"class": "form-control", "id": "password1",
                                                                    "autocomplete": "off", "placeholder": "设置您的新密码"}))
    password2 = forms.CharField(label="密 码2",
                                widget=widgets.PasswordInput(attrs={"class": "form-control", "id": "password2",
                                                                    "autocomplete": "off", "placeholder": "请再次输入密码"}))

    def clean(self):
        if self.cleaned_data.get("password1") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")
