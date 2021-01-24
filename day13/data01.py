import ddt
import time
from selenium import webdriver
import unittest
#测试类前用@ddt.ddt说明。测试方法前使用@data(1,2,3)添加数据
from ddt import ddt,data,unpack

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

#参数函数封装
@ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data({'a':1,'b':2})
    @unpack
    def test_qw(self,a,b):
        d = sub(a,b)
        print('d:',d)


    @data([2,2,4])
    #@data((2,2,4))    @可以是元组、列表、字典形式的
    @unpack    #用来切割，使[2,2,4]作为3个参数传入；如果不调用@unpack，会把整个列表当做一个参数传入
    def test_er(self,a,b,c):
        d = add(a,b)
        print('d:',d)
        #self.assertEqual(d,c,'通过')       #2种断言方式
        assert d == c

    #@data(*[{'a':1,'b':1},{'a':2,'b':2},{'a':3,'b':3}])  #列表里面嵌套字典分割； 使用 * 可以把列表、字典嵌套内容分割成各个元组，然后依次把元组传参
    #@data(*((1,2),(2,3))) #元组里面嵌套元组分割
    #@data(*[[2,3],[3,4]])  #列表里面嵌套列表分割
    #@data(*[(1,2),(2,3)])  #列表里面嵌套元组分割
    @data(*[(1,2,3),(2,2,4),(3,2,5)])
    @unpack
    def test_as(self,a,b,c):
        e = add(a,b)
        print('e:',e)
        #self.assertEqual(e,c)
        assert e ==c

    # @data((1,2,3),(2,2,4),(3,2,4))   #直接传入多个元组
    #@data({'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'b': 3, 'c': 5}, {'a': 3, 'b': 3, 'c': 7})
    @data([1,2,3],[2,3,4],[2,3,5])
    @unpack
    def test_qa(self,a,b,c):
        print(a,b,c)
        if a+b ==c:
            print(True)
        else:
            print(False)


if __name__=='__main__':
    #unittest.main(verbosity=2)
    unittest.main(verbosity=1)
