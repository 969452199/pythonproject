import pytest
def add(a,b):
    return a+b

# @pytest.mark.parametrize('a',(1,2,3,4,5))
# def test_add(a):
#     print('\na的值：',a)
#     assert add(a,1) == a +1

@pytest.mark.parametrize('a,b,c',[(1,2,3),(4,5,9),('1','2','12')])
def test_add1(a,b,c):
    print(f'\na,b,c的值：{a},{b},{c}')
    print('a+b=',a+b)
    assert add(a,b) == c

if __name__=='__main__':
    pytest.main(['-v','-s','pytest01.py'])


