from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
text1 = driver.find_element_by_class_name('soutu-hover-tip').text
print(text1)
title1 = driver.title
print(title1)

la = driver.current_url
print(la)

ef = driver.find_element_by_id('su').get_attribute('class')
print(ef)



driver.find_element_by_id('kw').send_keys('git获取参数')
a = driver.find_element_by_id('kw').is_displayed()
print(a)
if a:
    print('可操作')
else:
    print('不可操作')

b = driver.find_element_by_id('kw').is_enabled()
print(b)
c = driver.find_element_by_id('su').size
print(c)

driver.find_element_by_id('su').click()
time.sleep(2)
# 后退
driver.back()
time.sleep(3)

# 前进
driver.forward()
time.sleep(3)
# 刷新
driver.refresh()
# 设置浏览器大小
# driver.set_window_size(300,300)
# # 设置浏览器位置
position = driver.set_window_position(300,200)
print("当前位置",position)
# # 关闭浏览器单个窗口
# driver.close()
# # 关闭浏览器所有窗口
#
# driver.quit()
pagesource = driver.page_source
print('网页源码：',pagesource)





