import numpy as np
import math

def calculate_bins(datas):
    q3, q1 = np.percentile(datas, [75, 25])
    iqr = abs(q3 - q1)
    bin_width = 2 * iqr * np.size(datas) ** (-1/3)
    bins_count = round((np.max(datas) - np.min(datas)) / bin_width)
    return bins_count

def standard_error(datas):
    return np.std(datas) / math.sqrt(np.size(datas))

double_sort = lambda a, b: [x for _,x in sorted(zip(a, b))]