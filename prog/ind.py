#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import threading

E = 10e-7


def calc_term(x,n):
    return ((-1) ** n) * ((x**(2*n)) / math.factorial(n))


def calc_sum(x, E):
    n = 0
    term = calc_term(x, n)
    total_sum = term
    while abs(term) >= E:
        n += 1
        term = calc_term(x, n)
        total_sum += term
    return total_sum


def control(x, contv):
    sumv = calc_sum(x, E)
    return sumv, sumv == contv


def main():
    x = -0.7
    contv = math.exp(-x**2)
    result = [0]

    th1 = threading.Thread(target=calc_term, args=(x, 0))
    th2= threading.Thread(target=calc_sum, args=(x, E))
    th3 = threading.Thread(target=lambda: result.append(control(x, contv)))

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

    print(f"Сумма ряда: {result[-1][0]}")


if __name__ == "__main__":
    main()