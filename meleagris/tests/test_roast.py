import numpy.testing as npt
from meleagris import roast

def test_roast():
	r = roast.roast_temp() 
	assert(isinstance(r, str))
