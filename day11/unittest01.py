import unittest
class TestCastes(unittest.TestCase):
    # @classmethod#装饰器，与下行一起用，整个测试套件只执行一次初始化设置，只结束一次
    # def setUpClass(cls):
    #     print('=======只初始化一次======')

#执行顺序按ACCII编码排序执行
    def setUp(self):
        print('初始化')

    def tearDown(self):
        print('结束')

    def test_case01(self):
        print('第一个用例')

    def test_case02(self):
        print('第二个用例')
    # @classmethod
    # def  tearDownClass(cls):
    #     print('====只结束一次=====')

if __name__ =='__main__':
    #unittest.main(verbosity=2)#第一种方法：全部用例执行
    suit = unittest.TestSuite() #第二种方法：指定用例执行，TestCastes为类名称
    suit.addTest(TestCastes('test_case01'))
    suit.addTest(TestCastes('test_case02'))
    unittest.TextTestRunner().run(suit)
