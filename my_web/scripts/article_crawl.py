import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.news.models import NewsList, NewsAuthor
from apps.videos.models import VideoList
import requests
import random
import sys
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
        # {"http": "117.191.11.74:80"},
        # {"http": "117.191.11.101:80"},
        # {"http": "106.75.140.205:8888"},
        # {"http": "117.191.11.105:80"},
        # {"http": "117.191.11.76:80"},
        {"http": "39.137.69.8:8080"},
        # {"http": "112.84.178.21:8888"},
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
    article_list = soup.select(".igao7-test-list > .item2")
    for article in article_list:
        url = article.a["href"]
        title = article.a["title"]
        pic = article.img["data-original"]
        desc = article.contents[3].contents[3].string.split()[0]
        if not NewsList.objects.filter(url=url):
            header_2, proxy_2 = set_conf()
            article_html = get_html(url, header_2, proxy_2)
            article_content, t = get_content_time(article_html)
            save_data(url, title, pic, desc, article_content, t)
        else:
            print("数据已存在")

def get_content_time(html):
    soup = BeautifulSoup(html, "lxml")
    article_list = soup.select(".content")
    article = str(article_list[0]).split("<hr")[0]
    print(article)
    article_time = soup.select(".datas > .time")
    t = article_time[0].get_text()
    print(t)
    return article, t


def save_data(url, title, pic, desc, content, t):
    print(url)
    print(title)
    print(pic)
    print(desc)
    print("="*100)
    author = NewsAuthor.objects.get_or_create(name="爱搞机")
    if title not in NewsList.objects.all():
        news = NewsList.objects.get_or_create(url=url, title=title, pic=pic, description=desc,
                                              author_id=author[0].id, content=content, make_time=t)
        news[0].save()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s---%(lineno)s----%(name)s: %(message)s",
        filename="article_crawl.txt",
        filemode="a"
    )
    url = "http://www.igao7.com/category/express/page/"
    for i in range(2):
        try:
            header, proxy = set_conf()
            html = get_html(url+str(i+1), header, proxy)
            get_soup(html)
            time.sleep(1)
        except Exception as ex:
            logging.debug(f'debug message：{ex}')


