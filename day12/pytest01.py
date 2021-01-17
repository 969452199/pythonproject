import pytest,random,os,time
#coding=utf-8

#pytest中用例必须以test开头

def test_case01():
    print('第一个用例')
#@pytest.mark.webtest #装饰器，只执行装饰器下的一条用例，如果需指定多条用例，需要一一对应输入装饰器；webtest随意命名
#@pytest.mark.flaky(reruns=2,reruns_delay=5)#固定语法，当存在失败案例时，重复执行，2次，每次间隔时长5秒
def test_case02():
    print('第二个用例')
    assert 1==2 #断言



class TestClass:
    def test_case03(self):
        print('第一个用例')

    def test_case04(self):
        print('第二个用例')
if __name__=='__main__':
    #pytest.main(['-v','pytest01.py'])#执行整个文件中的所有用例
    #pytest.main(['-v','-s','-k=case04','pytest01.py'])#-k=  执行匹配关键字的用例,如-k=case04
    #pytest.main(['-v','pytest01.py'])#装饰器，只执行装饰器下的一条用例，如果需指定多条用例，需要一一对应输入装饰器；webtest随意命名
    pytest.main(['-v', '-s', 'pytest01.py', '--alluredir', './allure-result', '--clean-alluredir'])
    # time.sleep(1)
    # os.system('xcopy .\\allure-result\public .\\allure-result /e /Y /I')
    time.sleep(1)
    os.system('allure generate ./allure-result -o ./allure-report --clean')
    time.sleep(1)
    os.system('xcopy .\\allure-report\history .\\allure-result\history /e /Y /I')

#pytest pytest01.py --reruns 5 --reruns-delay 10 -s   文件pytest01.py中失败案例重跑5次，间隔10秒，可在路径cdm执行命令