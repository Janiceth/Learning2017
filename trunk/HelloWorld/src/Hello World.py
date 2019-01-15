

# print "Hello world!"
#coding=utf-8
# animalslist=['fox', 'tiger', 'rabbit', 'snake']
# print "I don't like these", len(animalslist), 'animals...'
#
# for items in animalslist:
#     print items
#
# animalslist.append('pig')
# del animalslist[0]
# animalslist.sort()
# for i in range(0, len(animalslist)):
#     print animalslist[i],

from selenium import  webdriver
import  time
driver= webdriver.Ie()
driver.get("http://bizhi.ludashi.com/live/page/")
time.sleep(15)

print(driver.find_elements_by_xpath('/html/body/div[1]/div[1]/a[3]'))
