#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

bro = webdriver.Chrome()
bro.get('https://sz.58.com/')
bro.maximize_window()
bro.implicitly_wait(30)#30秒内没出现元素会报错
bro.find_element_by_link_text('个人房源').click()
time.sleep(4)
#bro.find_element_by_css_selector('body > div.article > div.mainWrap > div.leftSide > div > div.fl.cbp1.cbhg > div:nth-child(1) > span:nth-child(8) > a')
#bro.current_window_handle()
le = bro.window_handles
for i in le:
    if i == bro.current_window_handle:
        le.remove(i)
bro.switch_to.window(le[0])
time.sleep(5)
ele = bro.find_elements_by_class_name('house-list')#获取房源列表
for e in ele:
    print(e.text)
