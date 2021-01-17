import time
import unittest
from selenium import webdriver
from day12 import logging03

log =logging03.logers(logging03.creat_file(),level='debug')
log.loger.debug('debug')

class LagouLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        log.loger.info('打开浏览器')
        cls.driver.get('https://www.lagou.com/')
        cls.driver.maximize_window()
        log.loger.info('窗口最大化')
        cls.driver.implicitly_wait(20)
#test_login01：输入正确账号，密码为空；
#test_login02：输入正确账号，输入错误密码；
#test_login03：输入正确账号，正确密码；

    def test_login01(self):
        dirver = self.driver
        ltt = self.driver.find_element_by_class_name('focus')
        if ltt:
            ltt.click()
            self.driver.find_element_by_class_name('login').click()
            time.sleep(2)
        else:
            self.driver.find_element_by_class_name('login').click()

        ltr = self.driver.find_elements_by_class_name('login_enter_password')
        time.sleep(2)
        ltr[0].send_keys('18702594561')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]').click()
        time.sleep(3)
        return_test = self.driver.find_element_by_class_name('input_tips').text
        print(return_test)
        log.loger.info('请输入密码')
        self.assertEqual(return_test,'请输入密码')
        time.sleep(4)

    def test_login02(self):
        ltr = self.driver.find_elements_by_class_name('login_enter_password')
        ltr[1].send_keys('18702594561')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]').click()
        time.sleep(3)
        return_test = self.driver.find_element_by_class_name('input_tips').text
        print(return_test)
        log.loger.info('账号和密码不匹配')
        self.assertEqual(return_test, '账号和密码不匹配')
        time.sleep(10)


    def test_login03(self):
        ltr = self.driver.find_elements_by_class_name('login_enter_password')
        ltr[1].clear()
        time.sleep(2)
        ltr[1].send_keys('xu187025945610')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]').click()
        time.sleep(6)
        return_test = self.driver.find_element_by_link_text('我的简历').text
        print('登录成功')
        self.assertEqual(return_test,'我的简历')
        time.sleep(2)

    def test_login04(self):
        self.driver.find_element_by_id('search_input').send_keys('软件测试')
        time.sleep(2)
        self.driver.find_element_by_id('search_button').click()
        lr = self.driver.find_element_by_class_name('body-btn')
        time.sleep(3)
        if lr:
            lr.click()
            lrt = self.driver.find_elements_by_class_name('hot-city-name')
            lrt[2].click()
        else:
            lrt = self.driver.find_elements_by_class_name('hot-city-name')
            lrt[2].click()
        log.loger.info('搜索软件测试岗位、深圳地区')
        time.sleep(3)

    def test_login05(self):
        lre = self.driver.find_elements_by_class_name('selectUI-text')
        lre[0].click()
        time.sleep(2)
        self.driver.find_element_by_link_text('15k-25k').click()
        time.sleep(3)
        lry = self.driver.find_elements_by_class_name('con_list_item')
        lry[0].click()
        log.loger.info('薪资范围15k-25k')




    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()


if __name__=='__main__':
    unittest.main()
