import numpy as np


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)

from scipy.ndimage import gaussian_filter
from scipy import misc

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

import pandas as pd

def ser():
    return pd.Series([1, 3, 5, np.nan, 6, 8])
