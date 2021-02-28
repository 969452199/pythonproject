import unittest
#from pages.risk.createRisk import CreateRisk
from selenium import webdriver
from day13.read_ini01 import ReadConf
import time

class TestCreateRisk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.lagou.com/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        time.sleep(3)
        #cls.risk = CreateRisk(cls.driver)
        # 读取配置文件,传入sections值，
        cls.url = ReadConf()
        cls.standard_url = cls.url.readConf('login') #这里传入risk模块
        # 获取配置文件中的url
        cls.base_url = cls.standard_url['username'] #这里传入risk模块中新建风险的url
        print(cls.base_url)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login01(self):
        ltt = self.driver.find_element_by_class_name('focus')
        if ltt:
            ltt.click()
            self.driver.find_element_by_class_name('login').click()
            time.sleep(2)
        else:
            self.driver.find_element_by_class_name('login').click()

        ltr = self.driver.find_elements_by_class_name('login_enter_password')
        time.sleep(2)
        ltr[0].send_keys(self.base_url)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]').click()
        time.sleep(3)
        return_test = self.driver.find_element_by_class_name('input_tips').text
        print(return_test)




if __name__ == '__main__':
    unittest.main()