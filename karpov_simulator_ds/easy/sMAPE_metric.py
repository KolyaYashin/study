import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:

    divider = 2 * np.abs(y_true - y_pred)
    denominator = np.abs(y_true) + np.abs(y_pred)
    not_zeros = (denominator != 0)
    ans = np.zeros(len(y_true))
    ans[not_zeros] = divider[not_zeros] / denominator[not_zeros]
    return np.mean(ans)
