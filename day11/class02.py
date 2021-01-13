from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.get_cookies()
driver.add_cookie({'name':'BAIDUID','value':'4EE3C044D4E600902A50F147650D53CA:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'TJxY1hSb09BQ3hjSnpLcDFmWThQNUVHNGVKaTRvYlE5dDVmTkpBSTNhUWYteUZnSVFBQUFBJCQAAAAAAAAAAAEAAAC6dt4mzvfA78730ce1xNPqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9u-l8fbvpfR'})
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.get_cookies()




