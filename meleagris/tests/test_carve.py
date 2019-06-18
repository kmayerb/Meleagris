import numpy.testing as npt
from meleagris import carve

def test_carve0():
	npt.assert_equal(carve.carve(1,5), 6)

def test_carve1():
	npt.assert_equal(carve.carve(1,1), 4)

def test_carve2():
	npt.assert_equal(carve.carve(1,0), 1)
