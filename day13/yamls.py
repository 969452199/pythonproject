import time,requests
import time
from selenium import webdriver

import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class UnitForTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("------类------前置条件")
    @classmethod
    def tearDownClass(cls):
        print("------类------后置条件")


    def setUp(self):
        print("------方法------前置条件")

    def tearDown(self):
        print("------方法------前置条件")
   # 测试用例默认以A-Z，a-z，0-9的顺序执行，与写的case顺序无关
    # def test_01(self):
    #     print("测试case")
    #     print('dfdfdfdf')
    #     # print(a)
    #
    @file_data('G:\\pythonproject\\test.yaml')
    def test_2(self, **user):
        print(user)

if __name__ == '__main__':
    unittest.main()
