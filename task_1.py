"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

Возьму для этого задачу 5 из третьего урока:
В массиве найти максимальный отрицательный элемент.


"""
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import random
import timeit
import cProfile

MAX_EL = 100
MIN_EL = -100
array1 = [random.randint(MIN_EL, MAX_EL) for _ in range(100)]
array2 = [random.randint(MIN_EL, MAX_EL) for _ in range(1000)]
array3 = [random.randint(MIN_EL, MAX_EL) for _ in range(10000)]
array4 = [random.randint(MIN_EL, MAX_EL) for _ in range(100000)]


def max_el(arr):
    max_index = -1
    for i in range(len(arr)):
        if arr[i] < 0:
            if max_index == -1:
                max_index = i
            elif (arr[i] > arr[max_index]):
                max_index = i
    return(max_index)


print('Замер первой функции')
result = max_el(array3)
if result == -1:
    print('отрицательных чисел в массиве нет')
else:
    print(
        f'Результат функции Номер элемента = {result} Значение элемента = {array3[result]}')

print(timeit.timeit('max_el(array1)', number=100,
      globals=globals()))  # 0.001048729000000026
print(timeit.timeit('max_el(array2)', number=100,
      globals=globals()))  # 0.011347496000000012
print(timeit.timeit('max_el(array3)', number=100,
      globals=globals()))  # 0.09723922099999999
print(timeit.timeit('max_el(array4)', number=100, globals=globals()))  # 0.95168492

cProfile.run('max_el(array4)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.011    0.011    0.011    0.011 tasl_1.py:23(max_el)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


def max_el1(arr):

    max_num = max(arr, key=lambda item: item if (item < 0) else -float("inf"))
    max_index = arr.index(max_num) if (max_num > -float("inf")) else -1
    return(max_index)


print('Замер второй функции')
result = max_el1(array3)
if result == -1:
    print('отрицательных чисел в массиве нет')
else:
    print(
        f'Результат функции Номер элемента = {result} Значение элемента = {array3[result]}')

print(timeit.timeit('max_el1(array1)', number=100,
      globals=globals()))  # 0.0017506540000000737
print(timeit.timeit('max_el1(array2)', number=100,
      globals=globals()))  # 0.016550748000000004
print(timeit.timeit('max_el1(array3)', number=100,
      globals=globals()))  # 0.14491595600000018
print(timeit.timeit('max_el1(array4)', number=100,
      globals=globals()))  # 1.4147221039999998

cProfile.run('max_el1(array4)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.031    0.031 <string>:1(<module>)
        1    0.000    0.000    0.031    0.031 tasl_1.py:61(max_el1)
   100000    0.016    0.000    0.016    0.000 tasl_1.py:63(<lambda>)
        1    0.000    0.000    0.031    0.031 {built-in method builtins.exec}
        1    0.015    0.015    0.031    0.031 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""


def max_el2(arr):

    arr_minus = [num for num in arr if num < 0]
    if len(arr_minus) > 0:
        max_num = max(arr_minus)
        max_index = arr.index(max_num)
    else:
        max_index = -1
    return(max_index)


print('Замер третьей функции')
result = max_el2(array3)
if result == -1:
    print('отрицательных чисел в массиве нет')
else:
    print(
        f'Результат функции Номер элемента = {result} Значение элемента = {array3[result]}')

print(timeit.timeit('max_el2(array1)', number=100,
      globals=globals()))  # 0.000651282999999836
print(timeit.timeit('max_el2(array2)', number=100,
      globals=globals()))  # 0.005811554999999746
print(timeit.timeit('max_el2(array3)', number=100,
      globals=globals()))  # 0.04771720299999993
print(timeit.timeit('max_el2(array4)', number=100,
      globals=globals()))  # 0.46038255699999997

cProfile.run('max_el2(array4)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 tasl_1.py:100(max_el2)
        1    0.004    0.004    0.004    0.004 tasl_1.py:102(<listcomp>)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""


"""
Исходя из анализа выполнения разных вариантов функции понятно, что основное время выполнения тратится на
перебор элементов массива. Попробуем этого избежать.
Единственное отличие - в этом случае мы возвращаем не индекс, а само значение максимального отрицательного числа
Индекс и порядок элементов утерян, зато, какая никакая, а победа в скорости выполнения.
"""


def max_el3(arr):
    arr.sort()
    if arr[0] >= 0:
        return(1)
    pos = len(arr) // 2
    left = 0
    right = len(arr) - 1
    while (right - left) > 1:
        if arr[pos] >= 0:
            right = pos
            pos = (left + right) // 2
        else:
            left = pos
            pos = (left + right) // 2
    return(arr[left])


print('Замер четвертой функции')
result = max_el3(array1)

if result == 1:
    print('отрицательных чисел в массиве нет')
else:
    print(
        f'Результат функции Номер элемента ПОТЕРЯН Значение элемента = {result}')

print(timeit.timeit('max_el3(array1)', number=100,
      globals=globals()))  # 0.00024077700000013635
print(timeit.timeit('max_el3(array2)', number=100,
      globals=globals()))  # 0.0011414339999999967
print(timeit.timeit('max_el3(array3)', number=100,
      globals=globals()))  # 0.007086939999999764
print(timeit.timeit('max_el3(array4)', number=100,
      globals=globals()))  # 0.07979819899999985


cProfile.run('max_el3(array4)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 tasl_1.py:151(max_el3)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}

"""


"""
И напоследок еще более разумная переделка.
Используем изначально правильно инструменты.
Создаем массив сразу с использованием NumPy

Это уже как факультатив, очень уж хотелось найти еще более быстрое решение
"""

MAX_EL = 100
MIN_EL = -100
np_array1 = np.array([random.randint(MIN_EL, MAX_EL) for _ in range(10)])
np_array2 = np.array([random.randint(MIN_EL, MAX_EL) for _ in range(1000)])
np_array3 = np.array([random.randint(MIN_EL, MAX_EL) for _ in range(10000)])
np_array4 = np.array([random.randint(MIN_EL, MAX_EL) for _ in range(100000)])


def max_el4(arr):
    return(np.where(arr < 0, arr, -np.inf).argmax())


print('Замер пятой функции')
result = max_el4(np_array1)

if array1[result] >= 0:
    print('отрицательных чисел в массиве нет')
else:
    print(
        f'Результат функции Номер элемента = {result} Значение элемента = {np_array1[result]}')


print(timeit.timeit('max_el4(np_array1)', number=100,
      globals=globals()))  # 0.0003895229999999472
print(timeit.timeit('max_el4(np_array2)', number=100,
      globals=globals()))  # 0.0010074249999996177
print(timeit.timeit('max_el4(np_array3)', number=100,
      globals=globals()))  # 0.007316043000000327
print(timeit.timeit('max_el4(np_array4)', number=100,
      globals=globals()))  # 0.06309545799999983


cProfile.run('max_el4(np_array4)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <__array_function__ internals>:2(where)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 multiarray.py:321(where)
        1    0.000    0.000    0.001    0.001 tasl_1.py:218(max_el4)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {method 'argmax' of 'numpy.ndarray' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


plt.title("Время поиска максимального отрицательного числа")  # заголовок
plt.xlabel("Количество элементов массива")  # ось абсцисс
plt.ylabel("Время выполнения")  # ось ординат
plt.grid()      # включение отображение сетки
x = np.array([100, 1000, 10000, 100000])


y1 = np.array([])
y1 = np.append(y1, timeit.timeit(
    'max_el(array1)', number=100, globals=globals()))
y1 = np.append(y1, timeit.timeit(
    'max_el(array2)', number=100, globals=globals()))
y1 = np.append(y1, timeit.timeit(
    'max_el(array3)', number=100, globals=globals()))
y1 = np.append(y1, timeit.timeit(
    'max_el(array4)', number=100, globals=globals()))

y2 = np.array([])
y2 = np.append(y2, timeit.timeit(
    'max_el1(array1)', number=100, globals=globals()))
y2 = np.append(y2, timeit.timeit(
    'max_el1(array2)', number=100, globals=globals()))
y2 = np.append(y2, timeit.timeit(
    'max_el1(array3)', number=100, globals=globals()))
y2 = np.append(y2, timeit.timeit(
    'max_el1(array4)', number=100, globals=globals()))

y3 = np.array([])
y3 = np.append(y3, timeit.timeit(
    'max_el2(array1)', number=100, globals=globals()))
y3 = np.append(y3, timeit.timeit(
    'max_el2(array2)', number=100, globals=globals()))
y3 = np.append(y3, timeit.timeit(
    'max_el2(array3)', number=100, globals=globals()))
y3 = np.append(y3, timeit.timeit(
    'max_el2(array4)', number=100, globals=globals()))

y4 = np.array([])
y4 = np.append(y4, timeit.timeit(
    'max_el3(array1)', number=100, globals=globals()))
y4 = np.append(y4, timeit.timeit(
    'max_el3(array2)', number=100, globals=globals()))
y4 = np.append(y4, timeit.timeit(
    'max_el3(array3)', number=100, globals=globals()))
y4 = np.append(y4, timeit.timeit(
    'max_el3(array4)', number=100, globals=globals()))

y5 = np.array([])
y5 = np.append(y5, timeit.timeit(
    'max_el4(np_array1)', number=100, globals=globals()))
y5 = np.append(y5, timeit.timeit(
    'max_el4(np_array2)', number=100, globals=globals()))
y5 = np.append(y5, timeit.timeit(
    'max_el4(np_array3)', number=100, globals=globals()))
y5 = np.append(y5, timeit.timeit(
    'max_el4(np_array4)', number=100, globals=globals()))

plt.plot(x, y1, label="Функция 1", c="b")  # построение графика
plt.plot(x, y2, label="Функция 2", c="g")  # построение графика
plt.plot(x, y3, label="Функция 3", c="y")  # построение графика
plt.plot(x, y4, label="Функция 4", c="orange")  # построение графика
plt.plot(x, y5, label="Функция 5", c="red")  # построение графика


plt.legend()
plt.show()
