#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

bro = webdriver.Chrome()
bro.get('https://tmall.com')
bro.maximize_window()
bro.implicitly_wait(30)#30秒内没出现元素会报错
bro.find_element_by_link_text('请登录').click()#链接型定位,以a开头的为链接型

#使用Xpath时，要整体放入,切换表单
bro.switch_to.frame(bro.find_element_by_xpath('//*[@id="J_loginIframe"]'))

#返回主页面
#bro.switch_to.default_content()

#一层一层切回
#bro.switch_to.parent_frame()

bro.find_element_by_name('fm-login-id').send_keys('西里西亚的雨')
bro.find_element_by_name('fm-login-password').send_keys('xu187025945610')
bro.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(5)

#如果账号密码不正确，获取报错文本（要输入报错定位）
#page = bro.find_element_by_xpath('').text

'''
#执行时报错，检查是否有嵌套表单或新表单，切换到子表单
bro.switch_to.frame(bro.find_element_by_xpath('//*[@id="J_LoginCheck"]/div/div/iframe'))

#注意等待时间，报错no such window，就把等待时间加长点
bro.find_element_by_xpath('//*[@id="J_GetCode"]').click()#点击获取验证码
time.sleep(4)
#输入验证码
testnumber = input('输入验证码')
bro.find_element_by_name('_fm.v._0.ph').send_keys(testnumber)
time.sleep(4)
bro.find_element_by_xpath('//*[@id="btn-submit"]').click()
'''
#if bro.find_element_by_xpath('//*[@id="login-info"]/span[1]/a[1]'):
#    print('成功')
#else:
#    print('失败')

#获取元素属性，判断是否存在来验证是否登录成功
a = bro.find_element_by_xpath('//*[@id="login-info"]/span[1]/a[1]').get_attribute('title')
assert (a =='西里西亚的雨')

bro.find_element_by_name('q').send_keys('良品铺子')
bro.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button').click()

bro.find_element_by_xpath('//*[@id="J_NavAttrsForm"]/div/div[1]/div[1]/div[2]/ul/li[1]/a/b').click()
bro.find_element_by_partial_link_text('【良品铺子香酥小黄鱼188g】').click()

bro.switch_to.window('https://detail.tmall.com/')
bro.find_element_by_id('J_LinkBasket').click()
bro.find_element_by_class_name('sn-cart-link').click()




