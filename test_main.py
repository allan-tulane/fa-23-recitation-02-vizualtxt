from main import *

def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(8, 2, 2) == 32
  assert simple_work_calc(6, 3, 2) == 24
  assert simple_work_calc(10, 5, 2) == 210

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(60, 6, 2, lambda n: n) == 13956
  assert work_calc(40, 2, 2, lambda n: n*n) == 3096
  assert work_calc(100, 2, 2,lambda n: 1) == 127
