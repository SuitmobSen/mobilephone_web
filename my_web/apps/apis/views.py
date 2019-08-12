from django.shortcuts import render, HttpResponse
from io import BytesIO
from libs import patcha
import base64
from django.http import JsonResponse
# Create your views here.
import logging

logger = logging.getLogger("apis")


def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type + base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)


def check_captcha(request):
    ret = {"code": 400, "msg": "验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code')
    session_captcha_code = request.session['captcha']
    print(post_captcha_code, "——", session_captcha_code)
    if post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
        print(ret["msg"])
    else:
        print(ret["msg"])
    return JsonResponse(ret)
