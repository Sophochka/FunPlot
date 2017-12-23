#!/usr/bin/env python3

"""My first python utility"""

import math
import inspect
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Type min X, max X and step
MIN_X = -10
MAX_X = 10
D_X = 0.1
# ---------------------------------------------


# Hint 1: Write here your own functions to handle exceptions, log or simplifier expresions
def safe_div(value):
    """Sample function"""
    try:
        # Hint 2: Use round() to get exact x values
        # Hint 3: Use float() to get exception instead of getting Inf 
        x = float(round(value, 1))
        y = 1/x
        print('x = ', x, '; y = ', round(y, 4))
        return y
    except ZeroDivisionError:
        print('x = ', x, '; y = error')
        return None


# ---------------------------------------------
DATA = (
    # Type functions to display after colon, point char, color:
    (lambda x: math.sin(x), '.', 'r'),
    # Hint 4: Skip wrong x values:
    (lambda x: math.sqrt(x) if x >= 0 else None, '*', 'b'),
    # Hint 5: Handle exceptions because wrong x values:
    (lambda x: safe_div(x), '+', 'g'),
)
# ---------------------------------------------


# Utils
def func_source(func):
    """Return function source string"""
    func_str = str(inspect.getsourcelines(func)[0])
    func_str = func_str[func_str.find(":")+1:func_str.find(",")].strip()
    return func_str


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
