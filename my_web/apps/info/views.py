from django.shortcuts import render, HttpResponse
import os
import json
from django.template import loader
from .models import PhoneModel, Params, Phone, BasicParams
from apps.news.models import NewsList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def phones(request):
    all_pic = Phone.objects.all()
    return render(request, "info/phone_info.html", {"all_pic": all_pic})


def phone_detail(request, id, phoneid):
    phone = PhoneModel.objects.get(id=phoneid)
    b_params = BasicParams.objects.get(id=phone.params_id)
    param = Params.objects.get(id=phone.params_id)
    sys_os = json.loads(param.basic).get('出厂系统内核', None)
    product_date = json.loads(param.basic).get('上市日期', None)
    size = json.loads(param.appearance).get('手机尺寸', None)
    weight = json.loads(param.appearance).get('手机重量', None)
    news = NewsList.objects.filter(content__icontains=phone.model.split(" ")[0][:2]).order_by("-make_time")[:10]
    rank = PhoneModel.objects.filter(hot_rank__isnull=False).order_by("hot_rank")[:30]
    kwgs = {
        "os": sys_os,
        "product_date": product_date,
        "size": size,
        "weight": weight,
        "rank": rank,
    }
    # 热门手机排行榜
    # print(phone.model.split(" ")[0][:2])
    # print(news)
    # print(news.count())
    if news.count() < 3:
        news = NewsList.objects.all().order_by("-make_time")[:10]
    return render(request, "info/phone_detail.html", {"phone": phone, "b_params": b_params, "news": news, "kwgs": kwgs})


def phone_list(request, id):
    brand = Phone.objects.get(id=id).name
    phones = PhoneModel.objects.filter(brand_id=id).order_by("-product_date")
    paginator = Paginator(phones, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'info/phones_list.html', {'contacts': contacts, "pagerange": paginator.page_range, "brand": brand})


def more_params(request, id, phoneid):
    phone = PhoneModel.objects.get(id=phoneid)
    params = Params.objects.get(id=phone.params_id)
    basic = json.loads(params.basic)
    screen = json.loads(params.screen)
    hardware = json.loads(params.hardware)
    net = json.loads(params.net)
    camera = json.loads(params.camera)
    appearance = json.loads(params.appearance)
    func = json.loads(params.function)
    pack = json.loads(params.pack)
    protect = json.loads(params.protect)
    kwgs = {
        "basic": basic,
        "screen": screen,
        "hardware": hardware,
        "net": net,
        "camera": camera,
        "appearance": appearance,
        "func": func,
        "pack": pack,
        "protect": protect,
    }
    html = loader.get_template('param_detail.html').render(
        {"kwgs": kwgs, "phone": phone})
    return HttpResponse(html)
