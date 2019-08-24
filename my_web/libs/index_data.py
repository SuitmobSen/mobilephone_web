from apps.videos.models import VideoList
from django.db.models import Count


# 最近更新的手机测评视频
def recent_video():
    result = VideoList.objects.all().order_by("-make_time")[:10]
    return result


