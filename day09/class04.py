
#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


bro = webdriver.Chrome()
bro.get('https://register.tmall.com/?spm=875.7931836/B.a2226mz.2.66144265iGvLcD')
bro.switch_to.frame(bro.find_element_by_id('J_Member'))
bro.find_element_by_id('J_AgreementBtn').click()
#bro.find_element(By.ID,'J_AgreementBtn').click()

#bro.find_element_by_name('mobile').send_keys('18702594561')

# 6.elements是取复数形式，可以用索引定位传值(借助工具查询tag总数与位置）--tag_name定位
ele = bro.find_elements_by_tag_name('input')#列表形式
print(len(ele))
ele[4].send_keys('18702594561')

time.sleep(5)
from selenium.webdriver import ActionChains

ta = bro.find_element_by_class_name('btn_slide')
ActionChains(bro).drag_and_drop_by_offset(ta,300,0).perform()