import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.videos.models import Author, VideoList
import requests
import random
import json
import time
from urllib import parse

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
    # print(url)
    response = requests.get(url, headers=header, proxies=proxy)
    response.encoding = "utf-8"
    html = json.loads(response.text)
    html_data = html.get("data").get("result")
    return html_data


def process_data(data, author):
    video_data = {}
    for result in data:
        if judge_author(author) == result.get("author", ""):
            # print(result)
            # 视频标题
            video_data["title"] = result["title"].replace('<em class="keyword">', "").replace("</em>", "")
            if "amp;" in video_data["title"]:
               video_data["title"] = video_data["title"].replace("amp;", "")
            # 视频ID
            video_data["aid"] = result["aid"]
            # 标签
            video_data["tag"] = result["tag"]
            # 时长
            if len(result["duration"].split(":")[-1]) == 1:
                video_data["duration"] = result["duration"].split(":")[0] + ":0" + result["duration"].split(":")[-1]
            else:
                video_data["duration"] = result["duration"]
            # # 标题
            #video_data["title"] = result['description']
            # 播放量
            video_data["play"] = result["play"]
            # 缩略图
            video_data["pic"] = "https:" + result["pic"]
            # 作者
            video_data["author"] = result['author']
            # 视频源地址
            video_data["url"] = result['arcurl']
            print(video_data)
            save_data(video_data)
            time.sleep(1)
            # exit(0)
    print("=" * 200)
    

def judge_author(author):
    if author == "搞机零距离":
        return "钟文泽"
    elif author == "HYK":
        return "我是HYK"
    else:
        return author


def save_data(data):
    print(f"正在开始写入——{data['title']}")
    title = data["title"]
    author = data["author"]
    aid = data["aid"]
    duration = data["duration"]
    pic = data["pic"]
    play = data["play"]
    url = data["url"]
    a = Author.objects.get_or_create(name=author)
    if not VideoList.objects.filter(url=url):
        VideoList.objects.get_or_create(title=title, author_id=a[0].id, aid=aid, duration=duration, pic=pic, play=play, url=url)
        print("=================数据写入成功=================")
    else:
        print("=================数据已存在=================")


if __name__ == "__main__":
    header, proxy = set_conf()
    author = ["科技美学", "小白测评", "搞机零距离", "VDGER唯界", "爱搞机", "UnboxTherapy", "ZEALER官方频道", "HYK",
              "老师好我叫何同学", "TESTV官方频道"]
    for a in author:
        url = "https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&&search_type=video&highlight=1&keyword=" + \
              str(parse.quote(a)) + "&page="
        for i in range(1, 8):
            data = get_html(url+str(i), header, proxy)
            process_data(data, a)
        # exit(0)
