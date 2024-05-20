#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для заданного значения x
# найти сумму ряда S с точностью члена ряда по
# абсолютному значению E = 10e-7 и произвести сравнение
# полученной суммы с контрольным значением функции
# для двух бесконечных рядов.

import math
import threading

E = 10e-7
results = [1]

# считаем целевой ряд y
def calc_sum(x):
    return math.exp(-(x**2))

# считаем числитель и кладём результат в res
def calc_chis(x, res):
    res.append(-x)

# считаем знаменатель и кладём результат в res
def calc_znam(n, res):
    res.append(n + 1)

def main():
    x = 1
    i = 0
    while math.fabs(results[-1]) > E:
        # создаём списки для возврата значений из потоков
        chis = []
        znam = []

        # Вычисляем числитель и знаменатель в отдельных потоках
        th1 = threading.Thread(target=calc_chis, args = (x, chis))
        th2 = threading.Thread(target=calc_znam, args = (i, znam))

        th1.start()
        th2.start()

        th1.join()
        th2.join()

        cur = chis[0] / znam[0]
        results.append(cur * results[-1])

        i += 1

    y = calc_sum(x)
    calculated_sum = sum(results)
    print(f"x = {x}")
    print(f"Ожидаемое значение y = {y}")
    print(f"Подсчитанное значение суммы ряда = {calculated_sum}")

if __name__ == "__main__":
    main()
