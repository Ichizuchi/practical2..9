#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from functools import lru_cache
import timeit


# Функция, вычисляющая факториал рекурсивно
def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


# Функция, вычисляющая число фибонначи рекурсивно
def fib_rec(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)


# Функция, вычисляющая факториал рекурсивно оптимитизирована с использованием lru_cache
@lru_cache
def factorial_rec_lru(n):

    if n == 0:
        return 1
    else:
        return n * factorial_rec_lru(n - 1)


# Функция, вычисляющая число фибонначи рекурсивно оптимитизирована с использованием lru_cache
@lru_cache
def fib_rec_lru(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_lru(n - 2) + fib_rec_lru(n - 1)


# Функция, вычисляющая факториал итеративно
def factorial_iter(n):

    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


# Функция, вычисляющая число фибонначи итеративно
def fib_iter(n):

    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


# Создание графика из точек и настройка окна
def create_graph(b, c, namegraph):

    plt.scatter(b, c, s=5)
    plt.title(namegraph)
    plt.xlabel("Число, переданное в функцию")
    plt.ylabel("Время работы функции")


# Замер времени выполнения функций для разных случаев
def func_time(case_func, size):

    time = []
    repeat = 50
    N = [i for i in range(30)]
    for n in N:
        timer = timeit.timeit(
            lambda: case_func[0](n),
            number=repeat
        ) / repeat

        time.append(timer)

    plt.figure(case_func[1], size)
    plt.subplots_adjust(left=0.25)
    create_graph(N, time, case_func[1])


if __name__ == '__main__':

    dpi = 100
    width_inches = (1680 / dpi) / 4
    height_inches = (850 / dpi) / 2
    size = (width_inches, height_inches)
    functions = {
        factorial_rec: "Factorial рекурсивный",
        factorial_rec_lru: "Factorial рекурсивный с @lru_cache",
        factorial_iter: "Factorial итеративный",
        fib_rec: "Fib рекурсивный",
        fib_rec_lru: "Fib рекурсивный c @lru_cache",
        fib_iter: "Fib итеративный"
    }
    for func_case in functions.items():
        func_time(func_case, size)

    # Показ графиков†
    plt.show()
