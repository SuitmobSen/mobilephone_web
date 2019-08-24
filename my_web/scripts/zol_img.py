import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.info.models import Params, BasicParams, Phone, PhoneModel


import json
import random
import time
import requests
from bs4 import BeautifulSoup
from lxml import etree

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


def get_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for i in f.readlines():
            data.append(json.loads(i))
    return data


def get_html(url, header, proxy):
    respoonse = requests.get(url, headers=header, proxies=proxy, timeout=5)
    # respoonse.encoding = "utf-8"
    html = respoonse.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('.big-pic-fl > img')
    if result:
        img_url = result[0]["src"]
    else:
        result = soup.select('.goods-card__pic > a')
        img_url = result[0].img["src"]
    print(img_url)
    return img_url


def get_img(url, header, proxy):
    respoonse = requests.get(url, headers=header, proxies=proxy, timeout=5).content
    os.chdir("E:\Python_code\Django\mobilephone_web\my_web\media\phone_img")
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(respoonse)
    print("爬取图片成功......")
    return filename


def save_data(filename, phone):
    if "（" not in phone and phone[-1] == "）":
        phone = phone.split("）")[0]
    p = PhoneModel.objects.get(model=phone)
    p.bimg = "phone_img/"+filename
    p.save()
    print("数据库录入成功")


if __name__ == "__main__":
    filename = "参数url.txt"
    data = get_data(filename)
    i = 0
    for item in data:
        # print(item)
        for phone in item:
            if "（" not in phone and phone[-1] == "）":
                model = phone.split("）")[0]
            else:
                model = phone
            if PhoneModel.objects.get(model=model).bimg == "phone_img/default.jpg":
                print(phone, item[phone])
                try:
                    header, proxy = set_conf()
                    img_url = get_html(item[phone], header, proxy)
                    header, proxy = set_conf()
                    filename = get_img(img_url, header, proxy)
                    save_data(filename, phone)
                except Exception as ex:
                    print(ex)
                time.sleep(3)
