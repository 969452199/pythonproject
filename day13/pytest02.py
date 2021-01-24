import pytest
def add(a,b):
    return a+b


@pytest.mark.parametrize('a,b,c',[(1,2,3),(4,5,9),('1','2','12')])#针对整个类中的2条案例循环3组参数，所以会输出6个结果
class TestAdd():

    def test_add1(self,a,b,c):
        print('a+b=',a+b)
        assert add(a,b) == c

    def test_add2(self,a,b,c):
        print('a+b=',a+b)
        assert add(a, b) == c

if __name__=='__main__':
    pytest.main(['-v','-s','pytest02.py'])