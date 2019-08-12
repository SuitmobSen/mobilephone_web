from django.shortcuts import render

# Create your views here.

def phones(request):
    return render(request, "info/phone_info.html")
