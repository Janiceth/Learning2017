# -*- coding:gb18030 -*-
# -*- coding:utf-8 -*-
# __author__ = ��Janice��
# __project__  = ��EyegicAPPTest��

import HTMLTestRunner
import time
import unittest
from selenium.webdriver.common.keys import Keys
from appium import webdriver

global driver


class EyegicTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass'

        # ��ʼ��
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '5f1f945c'  # �ֻ��豸���ƣ�ͨ��adb device�鿴��
        desired_caps['platformVersion'] = '6.0.1'  # Androidϵͳ�汾��
        desired_caps['appPackage'] = 'com.idealsee.yixun'  # APK����
        desired_caps['appActivity'] = 'com.idealsee.ar.activity.ActivityTMain'  # APK��launcherActivity
        desired_caps['unicodeKeyboard'] = True  # ʹ��Unicode���뷽ʽ�����ַ���\
        desired_caps['resetKeyboard'] = True    # ���ؼ���

        command0 ='adb shell ime list -s'#�г��ֻ����е����뷨
        command1 ='adb shell ime set io.appium.android.ime/.UnicodeIME'#appium���뷨
        command2 ='adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'#�ѹ����뷨

1

        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()
        print 'tearDownClass'

    def setUp(self):
        print 'setUp'

    def tearDown(self):
        print 'tearDown'

    def FeedBack(self):
        print 1
        time.sleep(5)
        tip_menu = self.driver.find_element_by_id("com.idealsee.yixun:id/iv_frag_tip_menu")
        tip_menu.click()
        time.sleep(2)
        menu_set = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_frag_menu_set")
        menu_set.click()

        time.sleep(2)
        feedback = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_set_feedback")
        feedback.click()

        feed_info = self.driver.find_element_by_id("com.idealsee.yixun:id/et_feed_info")
        feed_info.click()
        feed_info.send_keys(u"3154356")

        feed_content = self.driver.find_element_by_id("com.idealsee.yixun:id/et_feed_content")
        feed_content.click()
        feed_content.send_keys(u"QQ+feed content")

        feed_done = self.driver.find_element_by_id("com.idealsee.yixun:id/btn_feed_done")
        feed_done.click()


    def ClearCache(self):
        print 2
        time.sleep(5)
        # driver.find_element_by_id("com.idealsee.yixun:id/iv_frag_tip_menu").click()
        # time.sleep(2)
        # driver.find_element_by_id("com.idealsee.yixun:id/tv_frag_menu_set").click()
        # time.sleep(2)
        clear = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_set_clear")
        clear.click()

        time.sleep(2)
        cache_ok = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_dlg_clear_cache_ok")
        cache_ok.click()

        set_return = self.driver.find_element_by_id("com.idealsee.yixun:id/btn_set_return")
        set_return.click()

    def DiscoverSearch(self):
        print 3
        time.sleep(2)
        menu = self.driver.find_element_by_id("com.idealsee.yixun:id/iv_frag_tip_menu")
        menu.click()

        time.sleep(2)
        discover = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_frag_menu_discover")
        discover.click()

        time.sleep(2)
        header_title = self.driver.find_element_by_id("com.idealsee.yixun:id/et_dicover_header_title")
        header_title.click()
        header_title.send_keys(u"��Ѷ")
        # driver.find_element_by_id("com.idealsee.yixun:id/et_dicover_header_title").send_keys(u"��Ѷ")

        time.sleep(2)
        praise = self.driver.find_element_by_id("com.idealsee.yixun:id/tv_item_random_praise")
        praise.send_keys(Keys.ENTER)

        # driver.quit()


# driver.find_element_by_class_name("android.widget.RelativeLayout").click()
# driver.find_element_by_xpath()

if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(EyegicTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestSuite()  # ����һ����Ԫ��������
    suite.addTest(EyegicTest("FeedBack"))    # �������������뵽����������
    suite.addTest(EyegicTest("ClearCache"))
    suite.addTest(EyegicTest("DiscoverSearch"))

    filename = "./eyegicReport.html"  # ��һ��������·����֧�����·��
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Eyegic_AutomatedTestReport',
                                           description='Eyegic_AutomatedTestReport')
    runner.run(suite)  # �Զ����в���

    fp.close()   # ���Ա���ر�
