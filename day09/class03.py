
#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


bro = webdriver.Chrome()
bro.get('https://register.tmall.com/?spm=875.7931836/B.a2226mz.2.66144265iGvLcD')
bro.switch_to.frame(bro.find_element_by_id('J_Member'))
bro.find_element_by_id('J_AgreementBtn').click()
#bro.find_element(By.ID,'J_AgreementBtn').click()

# 4.name定位
bro.find_element_by_name('mobile').send_keys('18702594561')

time.sleep(5)

#拖动鼠标，导入模块
from selenium.webdriver import ActionChains

# 5.class_name定位，当值有空格时，只能选部分值
ta = bro.find_element_by_class_name('btn_slide')
ActionChains(bro).drag_and_drop_by_offset(ta,300,0).perform()



