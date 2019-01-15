#!/usr/bin/python
# coding=utf-8

import os
import time
import logging
import unittest
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class CrashDemoTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '23', 'deviceName': '4d578caf', 'app': PATH('E:\\Learning\\Outcomes\\Crash_Demo_Test\\crash_demo-3.27.apk'),
                         'appPackage': 'com.idealsee.sdk.demo',
                        'appActivity': 'com.idealsee.sdk.demo.DemoActivity'}
        #
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.remove_app('com.idealsee.sdk.demo')
        self.driver.quit()

    def test_crash_demo(self):
        # time.sleep(20)
        self.driver.find_element_by_id('com.idealsee.sdk.demo:id/btn_activity_in_bottom').click()
        time.sleep(30)
        button = None
        try:
            button = self.driver.find_element_by_id("android:id/button1")
        except Exception, e:
            logging.info("Next Step!")
        if button is not None:
            button.click()
            # logging.error("Failed, Crash")
            self.assertTrue(False, "Failed, Crash")
        else:
            test_result = self.driver.find_element_by_id("com.idealsee.sdk.demo:id/test_pass_tv")
            self.assertEquals("pass", test_result.text)
            # logging.info("Passed, No Crash!")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(StartEyegicTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestSuite()
    suite.addTest(CrashDemoTests('test_crash_demo'))
