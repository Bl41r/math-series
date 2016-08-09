# -*- coding: utf-8 -*-
from __future__ import print_function
import sys


def fibonacci_iter(n):
    """Return the nth value of the Fibonacci series, using an iterative approach."""
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
    """Return the nth value of the Fibonacci series, using a recursive approach."""
    try:
        n = int(n)
    except:
        print(u"Please enter a valid integer.")
        return -2
    else:
        if n < 1:
            print(u"Please enter an integer greater than or equal to 1.")
            return -1
        if n < len(series):
            return series[n - 1]
        else:
            series.append(series[-1] + series[-2])
            return fibonacci_rec(n, series)


def lucas(n):
    """Return the nth value of the Lucas series."""
    series = [2, 1]
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


def sum_series(n, first=0, second=1):
    """Return the nth value of a custom sum series starting at 'first' and 'second'."""
    series = [first, second]
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


def main():
    """Linter is stupid."""
    if len(sys.argv) > 2:
        print(u'usage: ./series.py')
        sys.exit(1)
    else:
        print(u'Welcome to the mathematical series python module.')
        print(u'Here are our available functions:')
        print(u"")
        print(u'1. Iterative Fibonacci: ' + fibonacci_iter.__doc__)
        print(u'usage:  fibonacci_iter(n)')
        print(u"")
        print(u'1. Recursive Fibonacci: ' + fibonacci_rec.__doc__)
        print(u'usage:  fibonacci_rec(n)')
        print(u"")
        print(u'1. Lucas: ' + lucas.__doc__)
        print(u'usage:  lucas(n)')
        print(u"")
        print(u'1. Custom Sum Series: ' + sum_series.__doc__)
        print(u'usage:  sum_series(n, first=0, second=1)')

if __name__ == '__main__':
    main()
