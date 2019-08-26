from django.shortcuts import render, HttpResponse
from apps.videos.models import VideoList
from apps.news.models import NewsList
from apps.info.models import PhoneModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import loader
# Create your views here.


def index(request):
    new_video = VideoList.objects.all().order_by("-make_time")[:12]
    new_news = NewsList.objects.all().order_by("-make_time")[:8]
    return render(request, "index/index.html", {'new_video': new_video, "new_news": new_news})


def search(request):
    keyword = request.GET.get("keyword", "")
    print(keyword)
    if keyword:
        s_type = request.GET.get("type", "")
        if s_type == "video":
            videos = VideoList.objects.filter(title__icontains=keyword).order_by("-make_time")
            if videos:
                paginator = Paginator(videos, 20)
                page = request.GET.get('page')
                try:
                    contacts = paginator.page(page)
                except PageNotAnInteger:
                    contacts = paginator.page(1)
                except EmptyPage:
                    contacts = paginator.page(paginator.num_pages)
                return render(request, 'index/search_base.html',
                              {'videos': contacts, "pagerange": paginator.page_range, "keyword": keyword})
            else:
                return render(request, 'index/search_base.html', {'videos': "暂无搜索结果", "keyword": keyword})
        elif s_type == "news":
            news = NewsList.objects.filter(title__icontains=keyword).order_by("-make_time")
            if news:
                paginator = Paginator(news, 20)
                page = request.GET.get('page')
                try:
                    contacts = paginator.page(page)
                except PageNotAnInteger:
                    contacts = paginator.page(1)
                except EmptyPage:
                    contacts = paginator.page(paginator.num_pages)
                return render(request, 'index/search_base.html',
                              {'news': contacts, "pagerange": paginator.page_range, "keyword": keyword})
            else:
                return render(request, 'index/search_base.html', {'news': "暂无搜索结果", "keyword": keyword})
        else:
            phones = PhoneModel.objects.filter(model__icontains=keyword).order_by("score_id")
            if phones:
                paginator = Paginator(phones, 20)
                page = request.GET.get('page')
                try:
                    contacts = paginator.page(page)
                except PageNotAnInteger:
                    contacts = paginator.page(1)
                except EmptyPage:
                    contacts = paginator.page(paginator.num_pages)
                return render(request, 'index/search_base.html',
                              {'phones': contacts, "pagerange": paginator.page_range, "keyword": keyword})
            else:
                return render(request, 'index/search_base.html', {'phones': "暂无搜索结果", "keyword": keyword})
    return render(request, "index/index.html")


def about(request):
    return render(request, "index/about.html")
