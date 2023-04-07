import pandas as pd
import numpy as np
import scipy.stats as sc


chat_id = 628156322 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    t = 29
    x = (-1)*x
    scale = 0.5 + x.min()
    D = 2.0/t/t
    return D *(sc.laplace.ppf(0.5-p/2)/n - scale), \
           D*(sc.laplace.ppf(0.5+p/2)/n - scale)
