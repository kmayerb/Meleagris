import numpy.testing as npt
from meleagris import carve

def test_carve():
    npt.assert_equal(carve.carve(1,3), 4)
