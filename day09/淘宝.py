#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

bro = webdriver.Chrome()
bro.get('https://www.taobao.com/')
bro.maximize_window()
bro.implicitly_wait(30)#30秒内没出现元素会报错
bro.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()

bro.find_element_by_id('fm-login-id').send_keys('西里西亚的雨')
bro.find_element_by_id('fm-login-password').send_keys('xu187025945610')
bro.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

bro.find_element_by_id('q').send_keys('三字经书')

bro.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
lists = bro.find_elements_by_css_selector('[data-category="auctions"]')
lists[0].click()
le = bro.window_handles
print(le)
for i in le:
    if i == bro.current_window_handle:
        le.remove(i)
print(le[0])
bro.switch_to.window(le[0])
bro.find_element_by_id('J_LinkBasket').click()
bro.find_element_by_id('mc-menu-hd').click()
# list2 = bro.find_elements_by_id('J_OrderList')
# print(list2)
# time.sleep(5)
# list2[0].click()
time.sleep(2)
lt = bro.find_elements_by_tag_name('label')
time.sleep(1)
lt[2].click()
time.sleep(2)
bro.find_element_by_xpath('//*[@id="J_Go"]/span').click()
