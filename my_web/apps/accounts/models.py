from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 继承自带的用户表，并重写
class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    qq = models.CharField(max_length=12, verbose_name="QQ号")
    avator_sor = models.ImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

