from django.shortcuts import render
from .models import VideoList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import View

# Create your views here.


def videos(request):
    contact_list = VideoList.objects.all().order_by("id")
    paginator = Paginator(contact_list, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'videos/videos.html', {'contacts': contacts, "pagerange": paginator.page_range})


class VideoPlay(View):
    def get(self, request, id):
        video = VideoList.objects.filter(aid=id)
        print(video)
        return render(request, "videos/video_play.html", {"id": id, "video": video[0]})
