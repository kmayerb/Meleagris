from meleagris import carve
from meleagris import roast

__all__ = [
    'roast',
    'carve'
    ]

# For a review of the basics of the __init__.py file

#__init__.py is what is invoked when the package is imported.

# We assume that scripts will invoke turkey with one of the following:

# import turkey as tk

# from turkey import *

# form turkey import module

# For example, turkey contain roast and carve methods.

# If a script imports turkey as tk, the module roast will only be available if we

# include "from turkey import roast" in the __init__.py. Doing so,
# will make it available and a script with import turkey as tk can invoke
# tk.roast.roast_temp(); but, tk.carve.carve() will not be available.

# from turkey import roast

#  __all__ =[] to specifies which modules are
# import to global namespace on "from turkey import *"

#__all__ = [
#    'roast',
#    'carve'
#    ]
