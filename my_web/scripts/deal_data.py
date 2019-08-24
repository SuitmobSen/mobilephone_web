import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_web.settings")  # website可以更改为自己的项目名称
django.setup()


from apps.info.models import PhoneModel
phones = PhoneModel.objects.all().order_by("id")
for phone in phones:
    if "（" not in phone.model and phone.model[-1] == "）":
        print("修改前", phone.model)
        phone.model = phone.model.split("）")[0]
        print("修改后", phone.model)
        phone.save()
        print("="*50)
