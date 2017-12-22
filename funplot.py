#!/usr/bin/env python3

"""My first python utility"""

import math
import inspect
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Type min X, max X and step
MIN_X = -10.0
MAX_X = 10.0
D_X = 0.1
# ---------------------------------------------
DATA = (
    # Type functions to display after colon, point char, color:
    (lambda x: math.sin(x), '.', 'r'),
    (lambda x: math.cos(x), '*', 'b')
)
# ---------------------------------------------

# Utils
def func_source(func):
    """Return function source string"""
    func_str = str(inspect.getsourcelines(func)[0])
    func_str = func_str[func_str.find(":")+1:func_str.find(",")].strip()
    return "y = " + func_str

# Init plot and captions
FIG, AX = plt.subplots()
AX.set_title('Fun Plot')
AX.set_xlabel('X')
AX.set_ylabel('Y')

# Draw data
X = np.arange(MIN_X, MAX_X, D_X)
for f in DATA:
    AX.plot(X, list(map(f[0], X)), f[1], color=f[2])

# Add legend and show  plot
AX.legend(list(map(func_source, (f[0] for f in DATA))))
plt.show()
