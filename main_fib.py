"""
    Вычисление  n-го элемента последовательности Фибаначи 
    Начало последовательости принять с n[0] n[1] = 1, 1
    Исключить повторное вычисление
    Само значение вычисляется рекурсией
"""


from functools import lru_cache


@lru_cache
def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else x


# передоваемый параметр позиции требуемого элемента
print(fib(100))