from django.db import models

# Create your models here.


# 品牌
class Phone(models.Model):
    name = models.CharField("品牌名称", max_length=10)
    pic_path = models.CharField("品牌logo图", max_length=100, default="info/images/brand/default.jpg")
    office_url = models.CharField("官方网站", max_length=100, null=True)

    class Meta:
        verbose_name = "手机品牌表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 详细参数表
class Params(models.Model):
    basic = models.TextField("基本参数", blank=True, null=True)
    screen = models.TextField("屏幕", blank=True, null=True)
    hardware = models.TextField("硬件", blank=True, null=True)
    net = models.TextField("网络与连接", blank=True, null=True)
    camera = models.TextField("摄像头", blank=True, null=True)
    appearance = models.TextField("外观", blank=True, null=True)
    function = models.TextField("功能与服务", blank=True, null=True)
    pack = models.TextField("手机附件", blank=True, null=True)
    protect = models.TextField("保修信息", blank=True, null=True)

    class Meta:
        verbose_name = "手机详细参数表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"基本参数、屏幕、硬件、网络与连接、摄像头、外观、功能与服务、手机附件、保修信息"


# 基本参数表
class BasicParams(models.Model):
    cpu = models.CharField("CPU", max_length=50, blank=True, null=True)
    back = models.CharField("后置", max_length=100, blank=True, null=True)
    front = models.CharField("前置", max_length=50, blank=True, null=True)
    memory = models.CharField("内存", max_length=50, blank=True, null=True)
    battery = models.CharField("电池", max_length=50, blank=True, null=True)
    screen = models.CharField("屏幕", max_length=50, blank=True, null=True)
    dpi = models.CharField("分辨率", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "手机基本参数表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"CPU：{self.cpu} 后置：{self.back} 前置：{self.front} " \
               f"内存：{self.memory} 电池：{self.battery} 屏幕：{self.screen} 分辨率：{self.dpi}"


class Comment(models.Model):
    total_score = models.CharField("总评分", max_length=5, blank=True, null=True, default="0.0")
    xjb = models.CharField("性价比", max_length=5, blank=True, null=True, default="0.0")
    xn = models.CharField("性能", max_length=5, blank=True, null=True, default="0.0")
    xh = models.CharField("续航", max_length=5, blank=True, null=True, default="0.0")
    wg = models.CharField("外观", max_length=5, blank=True, null=True, default="0.0")
    pz = models.CharField("拍照", max_length=5, blank=True, null=True, default="0.0")
    phone = models.CharField("对应机型", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "ZOL网友评分表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"性价比：{self.xjb}，性能：{self.xn}，续航：{self.xh}，外观：{self.wg}，拍照：{self.pz}"


class PhoneModel(models.Model):
    brand = models.ForeignKey(Phone, verbose_name="所属品牌")
    model = models.CharField("手机型号", max_length=100)
    product_date = models.DateField("上市日期", null=True, blank=True)
    price = models.CharField("ZOL报价", max_length=10, default="暂无报价")
    hot_rank = models.IntegerField("热门排行榜", null=True, blank=True)
    jd_url = models.CharField("京东入口", max_length=100, default="https://www.jd.com")
    jd_price = models.CharField("京东报价", max_length=10, default="暂无报价")
    jd_goodrate = models.CharField("京东好评率", max_length=10, default="暂无数据")
    sn_goodrate = models.CharField("苏宁好评率", max_length=10, default="暂无数据")
    description = models.TextField("信息简述")
    img = models.ImageField("手机缩略图", upload_to="media/phones/", default='phones/default.jpg')
    bimg = models.ImageField("展示图", upload_to="media/phone_img/", default='phone_img/default.jpg')
    params = models.OneToOneField(Params, verbose_name="手机详细参数", related_name="phones")
    basicparams = models.OneToOneField(BasicParams, verbose_name="手机基本参数", related_name="phone")
    score = models.OneToOneField(Comment, verbose_name="网友评分", null=True, blank=True)

    class Meta:
        verbose_name = "手机信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.brand}：{self.model}"












