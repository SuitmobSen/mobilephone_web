import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

import os
import json
import random
import requests
from bs4 import BeautifulSoup
import time
from apps.info.models import PhoneModel, Comment

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
    respoonse = requests.get(url, headers=header, proxies=proxy, timeout=5)
    # respoonse.encoding = "utf-8"
    html = respoonse.text
    # print(html)
    print("正在爬取数据")
    return html


def get_param(html, phone):
    jd_url = "https://www.jd.com"
    jd_price = "暂无报价"
    xjb = ""
    xn = ""
    xh = ""
    wg = ""
    pz = ""
    jd_goodrate = "暂无数据"
    sn_goodrate = "暂无数据"
    total_score = ""
    soup = BeautifulSoup(html, "lxml")
    # 京东商店入口 及 价格
    div = soup.select(".b2c-jd")
    if div:
        jd_url = div[0].a["href"].split("=")[-1]
        jd_price = div[0].span.span.get_text()
        print(jd_url, jd_price)
    # 电商好评率
    good = soup.select(".product-b2cgoodrate > li")
    if good:
        jd_goodrate = good[0].span.get_text()
        # sn_goodrate = good[1].span.get_text()
        print(jd_goodrate)
    # ZOL网友评分
    # comment = soup.select(".features-score > div > a")
    # if comment:
    #     xjb = comment[0].div.get_text()
    #     xn = comment[1].div.get_text()
    #     xh = comment[2].div.get_text()
    #     wg = comment[3].div.get_text()
    #     pz = comment[4].div.get_text()
    #     print(xjb, xn, xh, wg, pz)
    score = soup.select(".total-score > strong")
    if score:
        total_score = score[0].get_text()
    else:
        score = soup.select(".price_lab > .red > strong > b")
        total_score = score[0].get_text()
    save_data(jd_url, jd_price, jd_goodrate, sn_goodrate, total_score, phone)


def save_data(jd_url, jd_price, jd_goodrate, sn_goodrate, total_score, phone):
    if "（" not in phone and phone[-1] == "）":
        phone = phone.split("）")[0]
    print(jd_url, jd_price, jd_goodrate, sn_goodrate, total_score)
    c = Comment.objects.get_or_create(total_score=total_score, phone=phone)
    p = PhoneModel.objects.get(model=phone)
    p.jd_url = jd_url
    p.jd_price = jd_price
    p.jd_goodrate = jd_goodrate
    p.sn_goodrate = sn_goodrate
    p.score_id = c[0].id
    p.save()
    print("数据录入成功")


if __name__ == "__main__":
    os.chdir("ZOL-data")
    dir_list = os.listdir(os.getcwd())
    for dir in dir_list:
        os.chdir(dir)
        file_list = os.listdir(os.getcwd())
        # print(file_list)
        for file in file_list:
            with open(file, "r", encoding="utf-8") as f:
                content = json.loads(f.read())
                # print(content)
                for phone in content:
                    if "（" not in phone and phone[-1] == "）":
                        model = phone.split("）")[0]
                    else:
                        model = phone
                    if not PhoneModel.objects.get(model=model).score_id:
                        try:
                            print(phone, ":", content[phone]["url"])
                            header, proxy = set_conf()
                            url = content[phone]["url"]
                            # url = "http://detail.zol.com.cn/cell_phone/index1258538.shtml"
                            html = get_html(url, header, proxy)
                            get_param(html, phone)
                        except Exception as ex:
                            print(ex)
                    # exit(0)
            time.sleep(2)
        os.chdir("../")

