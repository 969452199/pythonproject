import time
import unittest
from selenium import webdriver


class LaGouLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.lagou.com/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_register_01(self):
        driver = self.driver
        ltt = self.driver.find_element_by_class_name('focus')
        time.sleep(3)
        if ltt:
            ltt.click()
            self.driver.find_element_by_class_name('register').click()
            time.sleep(2)
        else:
            self.driver.find_element_by_class_name('register').click()
        lts = self.driver.find_elements_by_class_name('register_enter')
        lts[0].send_keys('18702594561')
        self.driver.find_element_by_id('register').click()
        ttest = self.driver.find_element_by_class_name('input_tips').text
        self.assertEqual(ttest,'请输入6位数字验证码')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=='__main__':
    unittest.main()