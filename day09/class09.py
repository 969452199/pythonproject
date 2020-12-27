

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
# handle = bro.current_window_handle


ActionChains(bro).move_to_element()