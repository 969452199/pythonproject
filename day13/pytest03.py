import pytest
def add(a,b):
    return a+b


data = [(1,2,3),(4,5,9),('1','2','12')]
idss = [f'data(d)' for d in range(len(data))]
@pytest.mark.parametrize('a,b,c',data,ids=idss)
def test_add(a,b,c):
    print(f'\na,b,c的值:{a},{b},{c}')
    assert add(a,b)==c

if __name__=='__main__':
    pytest.main(['-v','-s','pytest03.py'])