#!/usr/bin/env python3

"""My first python utility"""

import math
import inspect
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# ---------------------------------------------
# INPUT DATA
# ---------------------------------------------
# Type function to display after colon
FUNCTION = lambda x: math.sin(x)

# Type min X, max X and step
MIN_X = -10.0
MAX_X = 10.0
D_X = 0.1
# --------------------------------------------- 

# --------------------------------------------- 
# APPEARANCE
# --------------------------------------------- 
CHAR = '.'
#matplotlib.rcParams['axes.unicode_minus'] = False
# --------------------------------------------- 


def func_source(func):
    """Return function source string"""
    func_str = str(inspect.getsourcelines(func)[0])
    func_str = func_str.strip("['\\n']").split(" = ")[1].split(":")[1].strip()
    return func_str


X = np.arange(MIN_X, MAX_X, D_X)
Y = list(map(FUNCTION, X))

fig, ax = plt.subplots()
ax.plot(X, Y, CHAR)
ax.set_title('Function: ' + func_source(FUNCTION))
plt.show()
