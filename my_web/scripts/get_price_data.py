import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.info.models import PhoneModel
import os
import json
import random
import requests
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


def get_img(url, header, proxy):
    response = requests.get(url, headers=header, proxies=proxy).content
    os.chdir("E:\Python_code\Django\mobilephone_web\my_web\media\phones")
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        print("正在存储", filename)
        f.write(response)
    return filename


if __name__ == "__main__":
    os.chdir("ZOL-data")
    dir_list = os.listdir(os.getcwd())
    for d in dir_list:
        os.chdir(d)
        file_list = os.listdir(os.getcwd())
        for file in file_list:
            with open(file, "r", encoding="utf-8") as f:
                content = json.loads(f.read())
                for p in content:
                    phone = PhoneModel.objects.get(model=p)
                    if phone.description == "无":
                        header, proxy = set_conf()
                        img_name = get_img(content[p]["s_img"], header, proxy)
                        phone.img = "phones/"+img_name
                        print("phones/"+img_name)
                        phone.description = content[p]["title"]
                        print(content[p]["title"])
                        phone.price = content[p]["ZOL_price"]
                        print(content[p]["ZOL_price"])
                        phone.save()
                        print("="*50)
                        print(os.getcwd())
                        os.chdir(f"E:\Python_code\Django\mobilephone_web\my_web\scripts\ZOL-data\{d}")
                        print(os.getcwd())
                        time.sleep(3)
                    # exit(0)
        os.chdir("../")
