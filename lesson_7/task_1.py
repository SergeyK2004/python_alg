"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).

Делаем классическим методом и затем пробуем два улучшения
Чтобы разобраться с улучшениями я сделал замер производительности на 50 000 элементов массива
Результаты замеров привел в конце кода

"""


import random
import timeit
import cProfile


def sort(arr):
    # классический метода пузырька
    arr = arr.copy()
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return [arr, n]


def sort1(arr):
    # классический метода пузырька оптимизированый на случай более раннего выстраивания массива чем полное
    # прохождение по N

    arr = arr.copy()
    n = 1
    while n < len(arr):
        need_break = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                need_break = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
        if need_break:
            break
    return [arr, n]


def sort2(arr):
    # Назовем это Пузырек с прицепом. Если большое число во время своего всплытия встречает другое большое число,
    # то "пузырек" тащит его за собой до конца.
    # Кроме этого используем переменную для обмена значений между элементами массива
    # на 5 000 элементов это экономит 0,1 секунды
    # И если пузырек тащит прицеп, сэкономим на одном лишнем присваивании и это еще -0,1 сек
    arr = arr.copy()
    n = 1
    while n < len(arr):
        need_break = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                need_break = False
                spam = arr[i + 1]
                arr[i + 1] = arr[i]
                if (i > 0) & (arr[i-1] < spam):
                    arr[i] = arr[i - 1]
                    arr[i - 1] = spam
                else:
                    arr[i] = spam

        n += 1
        if need_break:
            break
    return [arr, n]


def sort3(arr):
    # Назовем это Пузырек с прицепом. Если большое число во время своего всплытия встречает другое большое число,
    # то "пузырек" тащит его за собой до конца
    # здесь классический вариант обмена значениями через кортеж
    arr = arr.copy()
    n = 1
    while n < len(arr):
        need_break = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                need_break = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                if (i > 0) & (arr[i-1] < arr[i]):
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
        n += 1
        if need_break:
            break
    return [arr, n]


MAX_EL = 100
MIN_EL = -100
count_el = 20
array = [random.randint(MIN_EL, MAX_EL - 1) for _ in range(count_el)]

if count_el < 21:
    # печатаем массивы только если они небольшие
    print('Исходный массив')
    print(array)
    print('*' * 30)
    print('Отсортированный массив методом пузырька')
    result = sort(array)
    new_array = result[0]
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(new_array)
    print('*' * 30)
    print('Отсортированный массив улучшенным методом пузырька')
    result = sort1(array)
    new_array = result[0]
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(new_array)
    print('*' * 30)
    print('Отсортированный массив методом пузырька с прицепом')
    result = sort2(array)
    new_array = result[0]
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(new_array)
else:
    # печатать большие массивы нет смысла, но есть смысл сделать замер времени выполнения сортировки
    print(f'Исходный массив состоит из {count_el} элементов')
    print('-' * 30)
    print('Отсортированный массив методом пузырька')
    result = sort(array)
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(f'Время выполнения сортировки: {timeit.timeit("sort(array)", number=50, globals=globals())}')
    print('-' * 30)
    print('Отсортированный массив улучшенным методом пузырька')
    result = sort1(array)
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(f'Время выполнения сортировки: {timeit.timeit("sort1(array)", number=50, globals=globals())}')
    print('-' * 30)
    print('Отсортированный массив методом пузырька с прицепом')
    result = sort2(array)
    count_n = result[1]
    print(f'Количество проходов по циклу: {count_n}')
    print(f'Время выполнения сортировки: {timeit.timeit("sort2(array)", number=50, globals=globals())}')
    # Еще несколько миллисекунд можно сэкономить если не создавать кортеж при замене значений, а использовать
    # переменную spam. Сравним два замера, первый через переменную, второй с использованием кортежа
    print('-' * 30)
    print('Замер производительности при обмене через переменную')
    cProfile.run('sort2(array)')
    print('Замер производительности при обмене через кортеж')
    cProfile.run('sort3(array)')

"""
Результаты замера производительности
Исходные значения констант:
MAX_EL = 10000
MIN_EL = -10000
count_el = 50_000


Исходный массив состоит из 50000 элементов
------------------------------
Отсортированный массив методом пузырька
Количество проходов по циклу: 50000
Время выполнения сортировки: 379.67228081300004
------------------------------
Отсортированный массив улучшенным методом пузырька
Количество проходов по циклу: 49407
Время выполнения сортировки: 392.58190741
------------------------------
Отсортированный массив методом пузырька с прицепом
Количество проходов по циклу: 24705
Время выполнения сортировки: 265.21022284900005
------------------------------
Замер производительности при обмене через переменную
         49413 function calls in 264.970 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  264.970  264.970 <string>:1(<module>)
        1  264.959  264.959  264.970  264.970 task_1.py:48(sort2)
        1    0.000    0.000  264.970  264.970 {built-in method builtins.exec}
    49408    0.011    0.000    0.011    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Замер производительности при обмене через кортеж
         49413 function calls in 280.330 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  280.330  280.330 <string>:1(<module>)
        1  280.320  280.320  280.330  280.330 task_1.py:75(sort3)
        1    0.000    0.000  280.330  280.330 {built-in method builtins.exec}
    49408    0.009    0.000    0.009    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0


"""