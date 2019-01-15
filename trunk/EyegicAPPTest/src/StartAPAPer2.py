# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘EyegicAPPTest’

import os, time, unittest
from appium import webdriver


#PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '6.0.1'  # 设备系统版本
desired_caps['deviceName'] = '5f1f945c'  #  设备名称

# desired_caps['app'] = PATH(r"E:\tests\GuoYuB2B_2.1.apk")
desired_caps['appPackage'] = 'com.idealsee.yixun'
desired_caps['appActivity'] = 'com.idealsee.ar.activity.ActivityTMain'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# time.sleep(5)


# desired_caps = {
#                 'platformName': 'Android',
#                 # 手机设备名称，通过adb device查看；
#                 'deviceName': '5f1f945c',
#                 # Android系统版本号
#                 'platformVersion': '6.0.1',
#                 # APK包名
#                 'appPackage': 'com.idealsee.yixun',
#                 # APK的launcherActivity
#                 'appActivity': 'com.idealsee.ar.activity.ActivityTMain',
#                 # 使用Unicode编码方式发送字符串
#                 'unicodeKeyboard': True,
#                 # 隐藏键盘
#                 # 'resetKeyboard': True
#                 }