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

def get_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for i in f.readlines():
            data.append(json.loads(i))
    return data


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
    respoonse = requests.get(url, headers=header, proxies=proxy)
    # respoonse.encoding = "utf-8"
    html = respoonse.text
    # print(html)
    return html


def get_param(html):
    result = etree.HTML(html)
    brand = result.xpath('//*[@id="_j_breadcrumb"]/text()')[0].split("手机")[0]
    soup = BeautifulSoup(html, "lxml")
    # 爬取详细参数
    table = soup.select(".detailed-parameters > table > tr")
    title = ""
    params = {}
    for i in table:
        if not i.th:
            title = i.td.get_text()
            params[title] = {}
        else:
            key = i.th.get_text().split()[0]
            value = "".join(i.td.span.get_text().split("\xa0")[0].split(">")).split("进入官网")[0]
            params[title][key] = value
    # 爬取基本参数
    info = soup.select(".wrapper > .info-list-fr > ul > li")
    basic = {}
    for li in info:
        key = li.div.label.get_text().split("：")[0]
        if li.div.a and '＞' not in li.div.a.get_text():
            value = li.div.a.get_text()
        else:
            value = li.div.span.get_text()
        basic[key] = value
    # print(params, basic)
    return brand, params, basic


def save_data(params, basics, phone, brand):
    print(f"正在写入—{phone}—数据")
    # 手机品牌
    brand = brand
    # 手机型号
    model = phone
    # 详细参数部分
    basic = json.dumps(params.get("基本参数", None))
    screen1 = json.dumps(params.get("屏幕", None))
    hardware = json.dumps(params.get("硬件", None))
    net = json.dumps(params.get("网络与连接", None))
    camera = json.dumps(params.get("摄像头", None))
    appearance = json.dumps(params.get("外观", None))
    function = json.dumps(params.get("功能与服务", None))
    pack = json.dumps(params.get("手机附件", None))
    protect = json.dumps(params.get("保修信息", None))
    # 基本参数部分
    cpu = basics.get("CPU", None)
    back = basics.get("后置", None)
    front = basics.get("前置", None)
    memory = basics.get("内存", None)
    battery = basics.get("电池", None)
    screen2 = basics.get("屏幕", None)
    dpi = basics.get("分辨率", None)
    x = Phone.objects.get_or_create(name=brand)
    y = Params.objects.create(basic=basic, screen=screen1, hardware=hardware, net=net, camera=camera,
                                     appearance=appearance, function=function, pack=pack, protect=protect)
    z = BasicParams.objects.create(cpu=cpu, back=back, front=front, memory=memory,
                                          battery=battery, screen=screen2, dpi=dpi)
    PhoneModel.objects.get_or_create(model=model, brand_id=x[0].id, params_id=y.id, basicparams_id=z.id)
    print("========================数据写入成功========================")


if __name__ == "__main__":
    filename = "参数url.txt"
    data = get_data(filename)
    flag = False
    for item in data:
        print(item)
        for phone in item:
            print(phone)
            if phone == "诺基亚2.1（全网通）":
                flag = True
                break
            if flag:
                print(f"正在爬取{phone}：{item[phone]}")
                header, proxy = set_conf()
                html = get_html(item[phone], header, proxy)
                brand, params, basic = get_param(html)
                save_data(params, basic, phone, brand)
        if flag:    # exit(0)
            time.sleep(5)
