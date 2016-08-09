from __future__ import print_function


def fibonacci_iter(n):
    series = [0, 1]
    i = len(series)
    try:
        n = int(n)
    except:
        print(u"Please enter a valid integer.")
        return -1
    finally:
        while n > i:
            series.append(series[i-1] + series[i-2])
            i += 1
        return series[n-1]


def fibonacci_rec(n, series=[0, 1]):
    try:
        n = int(n)
    except:
        print(u"Please enter a valid integer.")
        return -1
    finally:
        if n < len(series):
            return series[n-1]
        else:
            return fibonacci_rec(n, series.append(series[len(series) - 1] + series[len(series) - 2]))
