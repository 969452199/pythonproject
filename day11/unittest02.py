import time
import unittest
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.lagou.com/')
driver.maximize_window()
driver.implicitly_wait(20)
