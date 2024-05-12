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

def calc_sum(x):
    return math.exp(-(x**2))

def calc_chis(x, n):
    return ((-1) ** n) * (x ** (2 * n))

def calc_znam(n):
    return math.factorial(n)

def main():
    x = -0.7
    results = [1] 

    i = 1
    while True:
        # Вычисляем числитель и знаменатель в отдельных потоках
        th1 = threading.Thread(target=lambda: results.append(calc_chis(x, i)))
        th2 = threading.Thread(target=lambda: results.append(calc_znam(i)))

        th1.start()
        th2.start()

        th1.join()
        th2.join()

        # Проверяем условие остановки
        if abs(results[-2] / results[-1]) < E:
            break

        i += 1

    y = calc_sum(x)
    calculated_sum = sum(results)
    print(f"x = {x}")
    print(f"Ожидаемое значение y = {y}")
    print(f"Подсчитанное значение суммы ряда = {calculated_sum}")

if __name__ == "__main__":
    main()
