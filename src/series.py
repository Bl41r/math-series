# -*- coding: utf-8 -*-
from __future__ import print_function


def fibonacci_iter(n):
    series = [0, 1]
    try:
        n = int(n)
    except:
        print(u"Please enter a valid integer.")
        return -2
    else:
        if n < 1:
            print(u"Please enter an integer greater than or equal to 1.")
            return -1
        while n > len(series):
            series.append(series[-1] + series[-2])
        return series[n - 1]


def fibonacci_rec(n, series=[0, 1]):
    print(series)
    try:
        n = int(n)
        if n < 1:
            print(u"Please enter an integer greater than or equal to 1.")
            return -2
    except:
        print(u"Please enter a valid integer.")
        return -1
    else:
        if n < len(series):
            return series[n - 1]
        else:
            series.append(series[-1] + series[-2])
            return fibonacci_rec(n, series)
