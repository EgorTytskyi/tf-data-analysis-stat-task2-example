import pandas as pd
import numpy as np
import scipy.stats as stats 


chat_id = 628156322 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mean = np.mean(x)
    std = np.sqrt(2)
    df = len(x) - 1
    t_value = stats.t.ppf((1 + p) / 2, df)
    se = std / np.sqrt(len(x))
    lower_bound = mean - t_value * se
    upper_bound = mean + t_value * se
    return (lower_bound, upper_bound)
