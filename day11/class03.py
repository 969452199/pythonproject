from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import base64

#元素是否存在
def isElement(driver,by,value):
    try:
        element = driver.find_element(by=by,value=value)
    except NoSuchElementException as e:
        print(e)
        return False
    else:
        return True


#读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def imgs():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.zhihu.com/signin?next=%2F")
    WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]')).click()
    WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_name("username")).send_keys("5415656")
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("password")).send_keys("5415656")
    WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')).click()

    time.sleep(6)
    driver.get_screenshot_as_file("D:/img/capture.png")

    if isElement(driver,By.CLASS_NAME,"Captcha-englishImg"):
        img = driver.find_element_by_class_name("Captcha-englishImg")
        img.screenshot('G:\\pythonproject\\screenpicture\\ele_capture.png')

        # 获取元素位置信息
        # left = img.location['x']
        # top = img.location['y']
        # right = left + img.size['width']
        # bottom = top + img.size['height']
        # im = Image.open('D:\\img\\capture.png')
        # im = im.crop((left, top, right, bottom))  # 元素裁剪
        # im.save('D:\\img\\ele_capture.png')  # 元素截图
        # time.sleep(3)
        bs4 = get_file_content("G:\\pythonproject\\screenpicture\\ele_capture.png")
        str_url = base64.b64encode(bs4)
        # code_jian.img_imgs(str_url)
        print(str_url)

    else:
        img = driver.find_element_by_class_name("Captcha-chineseImg")
        img.screenshot('G:\\pythonproject\\screenpicture\\ele_capture.png')

        # 获取元素位置信息
        # left = img.location['x']
        # top = img.location['y']
        # right = left + img.size['width']
        # bottom = top + img.size['height']
        # im = Image.open('D:\\img\\capture.png')
        # im = im.crop((left, top, right, bottom))  # 元素裁剪
        # im.save('D:\\img\\ele_capture.png')  # 元素截图
        # time.sleep(2)
        bs4 = get_file_content("G:\\pythonproject\\screenpicture\\ele_capture.png")
        str_url = base64.b64encode(bs4)
        # code_jian.wenzi(str_url)
        print(str_url)




if __name__ == "__main__":
    imgs()

# 川石王刚 下午 12:10:26
# #coding:utf-8
# import urllib, sys
# import requests,base64
#
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# appcode = '3708C4AE94090809CA1F85262A9960AB'
# appKey = 'AKID790e16686379ae5916c3e15cea2bf5cb'
# appSecret = 'ec40c7d9891309eca896f5ac19b69a8d'
# host = 'http://apigateway.jianjiaoshuju.com'
#
# def img_imgs(str_url):
#     path = '/api/v_1/fzyzm.html'
#     bodys = {"v_pic":str_url,"v_type":"cn"}
#     url = host + path
#     header = {'appcode':appcode,'appKey':appKey,'appSecret':appSecret,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
#     res = requests.post(url,data=bodys,headers=header)
#     print(res.json())
#
# def wenzi(str_url):
#     path = '/api/v_1/charRecognized.html'
#     bodys = {"v_pic":str_url}
#     url = host + path
#     header = {'appcode': appcode, 'appKey': appKey, 'appSecret': appSecret,
#               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
#     res = requests.post(url, data=bodys, headers=header)
#     print(res.json())
#
#
# if __name__ == "__main__":
#     bs4 = get_file_content("D:\\img\\ele_capture.png")
#     str_url = base64.b64encode(bs4)
#     wenzi(str_url)

