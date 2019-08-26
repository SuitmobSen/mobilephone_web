import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()

from apps.info.models import PhoneModel

phones = PhoneModel.objects.filter(jd_url="www.jd.com")
print(phones)
print(phones.count())
# for phone in phones:
#     phone.jd_url = "https://www.jd.com"
#     phone.save()