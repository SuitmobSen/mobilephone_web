from django.db import models
from apps.videos.models import Tag
# Create your models here.


class NewsAuthor(models.Model):
    name = models.CharField("作者", max_length=20)

    class Meta:
        verbose_name = "文章作者表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NewsList(models.Model):
    title = models.CharField("标题", max_length=100)
    description = models.TextField("文章描述")
    content = models.TextField("文章内容", null=True)
    author = models.ForeignKey(NewsAuthor, verbose_name="文章作者")
    pic = models.ImageField("文章缩略图", upload_to="news/", default='news/default_300x300.jpg', max_length=200)
    url = models.CharField("文章源地址", max_length=100)
    tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    make_time = models.CharField("上传时间", max_length=20,  null=True, blank=True)
    pub_time = models.DateTimeField("入库时间", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "机情快讯列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.author}> {self.title}"