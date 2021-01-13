from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(30)

#复制粘贴
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
driver.get('http://cn.bing.com')
time.sleep(4)
driver.find_element_by_id('sb_form_q').send_keys(Keys.CONTROL,'v')
time.sleep(4)
driver.find_element_by_id('sb_form_go').click()
time.sleep(2)
#driver.find_element_by_id('sb_form_go').send_keys(Keys.ESCAPE,'Esc')
#driver.find_element_by_id('sb_form_go').send_keys('Keys.')删除待验证
#for i in range(10):  循环10次截图
driver.get_screenshot_as_file('../screenpicture/'+str(time.time())+'.png')#可封装成函数，只需传入路径(不要忘了斜杠）





