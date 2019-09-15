import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.news.models import NewsList, NewsAuthor
from apps.videos.models import VideoList
import requests
import random
from bs4 import BeautifulSoup
import json
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
        # {"http": "117.191.11.74:80"},
        # {"http": "117.191.11.101:80"},
        {"http": "106.75.140.205:8888"},
        # {"http": "117.191.11.105:80"},
        # {"http": "117.191.11.76:80"},
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
    response.encoding = "utf-8"
    html = response.text
    return html


def get_soup(html):
    soup = BeautifulSoup(html, "lxml")
    article_time = soup.select(".datas > .time")
    t = article_time[0].get_text()
    return t


if __name__ == "__main__":
    news = NewsList.objects.all().order_by("id")
    for new in news:
        if not new.make_time:
            try:
                header, proxy = set_conf()
                html = get_html(new.url, header, proxy)
                data = get_soup(html)
                print(data)
                new.make_time = data
                new.save()
            except Exception as ex:
                print(ex)
            time.sleep(1)