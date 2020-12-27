#coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import random
driver = webdriver.Chrome()
driver.get('https://sz.58.com/')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_link_text('个人房源').click()

driver.switch_to.window(driver.window_handles[-1])

lt = driver.find_elements_by_class_name('moniselectcon')
time.sleep(3)
acction = ActionChains(driver).move_to_element(lt[0]).perform()
lt1 = driver.find_elements_by_css_selector('#secitem-direction>a')
time.sleep(3)
# a = lt1[random.choices(lt1)
# a.click()
lt1[random.randint(0,len(lt1)-1)].click()
time.sleep(3)

ltt = driver.find_elements_by_class_name('moniselectcon')
acction1 = ActionChains(driver).move_to_element(ltt[1]).perform()
time.sleep(3)
lt2 = driver.find_element_by_xpath('//*[@id="secitem-direction"]/a')

lt2[random.randint(0,len(lt2)-1)].click()
driver.refresh()
time.sleep(3)










