import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

import requests
import random
from bs4 import BeautifulSoup
from apps.info.models import PhoneModel


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
    # response.encoding = "utf-8"
    html = response.text
    return html


def get_soup(html):
    soup = BeautifulSoup(html, "lxml")
    phone_rank = soup.select(".rank__name")
    print(len(phone_rank))
    for i, phone in enumerate(phone_rank):
        model = phone.a.get_text()
        if model[-1] == " ":
            model = " ".join(phone.a.get_text().split(" ")[:-1])
        print(f"【{i+1}】", model)
        save_data(model, i+1)
        # break


def save_data(phone, i):
    try:
        p = PhoneModel.objects.get(model=phone)
        p.hot_rank = i
        p.save()
        print("数据录入成功")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    url = "http://top.zol.com.cn/compositor/57/cell_phone.html"
    header, proxy = set_conf()
    html = get_html(url, header, proxy)
    get_soup(html)