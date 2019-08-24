import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()


from apps.videos.models import VideoList
import random
import requests
from bs4 import BeautifulSoup
import logging
import time

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
    response = requests.get(url, headers=header, proxies=proxy)
    html = response.text
    return html


def get_time(html):
    soup = BeautifulSoup(html, "lxml")
    times = soup.select(".video-data > span")
    data_time = times[1].string.split(" ")[0]
    return data_time


if __name__ == "__main__":
    videos = VideoList.objects.all().order_by("id")
    flag = False
    i = 0
    for video in videos:
        if not video.make_time:
            # flag = True
            i+=1
    print(i)
        # if video.title == "搞机零距离：锤子坚果R1白色上手 快去取消黑色版本的订单！":
        #     flag = True
        # if flag:
        #     try:
        #         header, proxy = set_conf()
        #         html = get_html(video.url, header, proxy)
        #         data_time = get_time(html)
        #         v = VideoList.objects.get(id=video.id)
        #         v.make_time = data_time
        #         v.save()
        #         print(video)
        #         print(data_time)
        #         print(video.url)
        #         print("="*100)
        #         time.sleep(1)
        #     except Exception as ex:
        #         print(ex)
