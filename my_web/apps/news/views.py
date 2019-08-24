from django.shortcuts import render
from .models import NewsList
from django.views.generic import View
from apps.info.models import PhoneModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def news(request):
    contact_list = NewsList.objects.all().order_by("id")
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'news/news.html', {'contacts': contacts, "pagerange": paginator.page_range})


class NewsDetail(View):
    def get(self, request, id):
        num = NewsList.objects.all().count()
        news = NewsList.objects.get(id=id)
        if news.id > 1:
            last = news.id - 1
        else:
            last = False
        if news.id == num:
            next = False
        else:
            next = news.id + 1
        kwgs = {
            "news": news,
            "last": last,
            "next": next,
        }
        print(news)
        return render(request, "news/news_detail.html", {"kwgs": kwgs})
