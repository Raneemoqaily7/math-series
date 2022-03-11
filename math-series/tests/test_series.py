from math_series.series import fibR
from math_series.series import lucas
from math_series.series import sum_series



def test_case0():
  actual=fibR(0)
  accepted =0
  assert actual == accepted 

def test_case1():
    actual =fibR(1)
    accepted=1
    assert actual==accepted

def test_case2():
    actual=fibR(2)
    accepted=1
    assert actual==accepted

    
def test_case3():
    actual=fibR(8)
    accepted=21
    assert actual==accepted 


# def test_case4():
   
#      #raise error
#     with pytest.raises(TypeError): #(Exception)
#         fibR("a")


def test_case5():
    actual =lucas(0)
    accepted = 2
    assert actual == accepted

def test_case6():
    actual =lucas(1)
    accepted = 1
    assert actual == accepted

def test_case7():
    actual =lucas(7)
    accepted = 29
    assert actual == accepted


def test_case8():
    actual=sum_series(2,0,1)
    accepted=1
    assert actual == accepted

def test_case9():
    actual=sum_series(3,2,1)
    accepted=4
    assert actual == accepted


def test_case9():
    actual=sum_series(3,3,5)
    accepted=1
    assert actual == accepted


def test_case9():
    actual=sum_series(1)
    accepted=1
    assert actual == accepted


def test_case9():
    actual=sum_series(0)
    accepted=0
    assert actual == accepted







    






