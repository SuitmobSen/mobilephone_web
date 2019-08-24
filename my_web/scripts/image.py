from PIL import Image
import os
os.chdir("E:\Python_code\Django\mobilephone_web\my_web\static\images\index_brand")

for i, file in enumerate(os.listdir(os.getcwd())):
    try:
        im = Image.open(file)
        (x, y) = im.size
        new_x = 264
        new_y = 142
        out = im.resize((new_x, new_y), Image.ANTIALIAS)
        out.save(fr"E:\Python_code\Django\mobilephone_web\my_web\apps\info\static\info\images\brand\pic{i+1}.jpg")
        print("成功转换")
    except Exception as ex:
        print("出错了:", ex)
        print(file)
# im = Image.open("blackshark.jpg")
# (x, y) = im.size
# new_x = 264
# new_y = 142
# out = im.resize((new_x, new_y), Image.ANTIALIAS)
# out.save(fr"E:\Python_code\Django\mobilephone_web\my_web\apps\info\static\info\images\brand\9blackshark.jpg")