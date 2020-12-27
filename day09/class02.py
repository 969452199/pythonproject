#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


bro = webdriver.Chrome()
bro.get('https://tmall.com')
bro.maximize_window()
bro.implicitly_wait(30)#30秒内没出现元素会报错
#bro.find_element_by_link_text('请登录').click()#链接型定位,以a开头的为链接型

# 1.超文本链接模糊定位 partial_link_text
bro.find_element_by_partial_link_text('注册').click()

# 2.超文本链接精准定位 link_text
#bro.find_element_by_link_text('免费注册').click()

# 3.id定位，有2种方式，by_id()/(By.ID,)
#bro.find_element_by_id('J_AgreementBtn').click()
#bro.find_element(By.ID,'J_AgreementBtn').click()

#超文本链接模糊定位
bro.find_element_by_partial_link_text('注册').click()

