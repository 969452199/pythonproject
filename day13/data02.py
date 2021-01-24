#coding=utf-8
import unittest,time
from ddt import ddt,data,unpack
from selenium import webdriver
import ddt
#适用场景：同一个用例，输入不同参数

#josn 文件可以是字典、列表


@ddt.ddt
class Douban(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        pass
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

        pass
    def setUp(self):
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        pass
    def tearDown(self):
        pass
    @ddt.file_data('G:\\pythonproject\\info.json')
    @ddt.unpack
    def test_baidu(self,value):
        print(value)
        can,yu = value.split('||')
        print(can,yu)
        time.sleep(2)
        self.driver.find_element_by_id('kw').send_keys(can)
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual(self.driver.title,yu)

if __name__ == '__main__':
    unittest.main()