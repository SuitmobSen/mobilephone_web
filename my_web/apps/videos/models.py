from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField("作者", max_length=20)

    class Meta:
        verbose_name = "视频作者表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("标签名", max_length=64)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"


class VideoList(models.Model):
    title = models.CharField("标题", max_length=100)
    author = models.ForeignKey(Author, verbose_name="视频作者")
    aid = models.IntegerField("视频ID")
    duration = models.CharField("视频时长", max_length=6)
    pic = models.CharField("缩略图", max_length=100)
    play = models.IntegerField("播放量")
    url = models.CharField("视频源地址", max_length=100)
    make_time = models.DateField("上传时间", null=True, blank=True)
    pub_time = models.DateTimeField("入库时间", auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name="视频标签", blank=True)
    img = models.ImageField("视频缩略图", upload_to="video/", default='video/default_300x300.jpg')

    class Meta:
        verbose_name = "视频列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"<{self.author}> {self.title}"

