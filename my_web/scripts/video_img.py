import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()


from apps.videos.models import VideoList
import random
import requests
from my_web.settings import MEDIA_ROOT
import json
import time
import logging
logger = logging.getLogger('script')


def set_conf():
    header_list = [
        # 遨游
        {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
        # 火狐
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
        # 谷歌
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"},
    ]
    proxy_ip = [
        {"http": "117.191.11.105:80"},
        # {"http": "182.92.242.11:80"},
        # {"http": "60.205.229.126:80"},
        # {"http": "60.190.250.120:8080"},
        # {"http": "111.231.94.44:8888"},
        {"http": "117.191.11.76:80"},
        {"http": "39.137.69.8:8080"},
        {"http": "112.84.178.21:8888"},
    ]
    header = random.choice(header_list)
    proxy = random.choice(proxy_ip)
    print(header)
    print(proxy)
    return header, proxy


def get_html(url, header, proxy):
    response = requests.get(url, headers=header, proxies=proxy).content
    filename = url.split("/")[-1]
    return response, filename

from PIL import Image


# 生成path图像的缩略图
def make_thumb(path, size):
    pixbuf = Image.open(path)
    width, height = pixbuf.size
    # 如果宽度大于size
    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)
        return pixbuf


def save_data(response, filename):
    os.chdir(r"E:\Python_code\Django\mobilephone_web\my_web\media\video_img")
    with open(filename, "wb+") as f:
        f.write(response)
    return filename
    # thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT+r"\video_img", filename), size=300)
    # if thumb_pixbuf:
    #     # 缩略图的保存文件全路径=> 保存文件
    #     img_name = filename.split(".")[0] + f'_{300}x{300}' + '.jpg'
    #     thumb_path = os.path.join(MEDIA_ROOT+r"\video_img", img_name)
    #     thumb_pixbuf.save(thumb_path)
    #     os.remove(filename)
    #     return r"video_img/" + img_name

if __name__ == "__main__":
    videos = VideoList.objects.all()
    flag = False
    i = 0
    for video in videos:
        if video.img != "video":
            i+=1
            print(video.pic)
            print(video)
    print(i)
        # if video.id == 1822:
        #     flag = True
        # if flag:
        #     try:
        #         print(video)
        #         header, proxy = set_conf()
        #         response, filename = get_html(video.pic, header, proxy)
        #         img_name = save_data(response, filename)
        #         a = VideoList.objects.get(id=video.id)
        #         a.img = img_name
        #         a.save()
        #         time.sleep(1)
        #     except Exception as ex:
        #         print(ex)
        #         logger.debug(f"{video.title}: {ex}")
        # exit(0)