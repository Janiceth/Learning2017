
# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
#
import media
from PIL import Image
#
# f = media.choose_file()
# pic = media.load_picture(f)
# media.show(p ic)
# 方式1
# img = Image.open('E:\\SVN\\Learning2017\\trunk\\HelloWorld\\src\\Mypsd_176994_201208111641100157B.jpg')
# img.show()

# 方式2：
pic = media.load_image('E:\\SVN\\Learning2017\\trunk\\HelloWorld\\src\\Mypsd_176994_201208111641100157B.jpg')
# media.show(pic)

media.crop_picture(pic, 150, 50, 450, 300)
media.show(pic)
media.save_as(pic, 'new1.jpg')

