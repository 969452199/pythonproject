#coding=utf-8
import unittest,time
from ddt import ddt,data,unpack
from selenium import webdriver
import ddt
#适用场景：同一个用例，输入不同参数

#josn 文件可以是字典、列表

qa = []
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
        self.dat = self.read_json()
        pass
    def tearDown(self):
        pass
    def read_json(self,file_path):
        with open(self.file_path = "G:\\pythonproject\\data.json") as fp:
            dat = json.load(fp)
            return dat
    def get_json(self,id):
        return self.dat[id]
        qa.append(dat[id])


    @ddt.file_data('G:\\pythonproject\\data.json')

    @ddt.unpack
    def test_baidu(self,key,value):
        print('sed')
        qa.append('sed')
        print(qa)
    #print(qa)

    # @data()
    # @ddt.unpack
    # def test_baidu(self,value):
    #     print(value)
    #     can,yu = value.split('||')
    #     print(can,yu)
    #     time.sleep(2)
    #     self.driver.find_element_by_id('kw').send_keys(can)
    #     time.sleep(2)
    #     self.driver.find_element_by_id('su').click()
    #     time.sleep(2)
    #     self.assertEqual(self.driver.title,yu)

if __name__ == '__main__':
    unittest.main(verbosity=2)