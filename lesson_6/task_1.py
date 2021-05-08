"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных 
программах в рамках первых трех уроков. Проанализировать результат и определить 
программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов 
кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к 
коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

Версия Python: Python 3.9.2
Mac OS: Darwin Kernel Version 20.4.0/RELEASE_X86_64 x86_64
"""

from timeit import timeit
import collections
import random
import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


def size_of(obj, res=0):
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                res += size_of(key, res)
                res += size_of(value, res)
        else:
            for item in obj:
                res += size_of(item, res)
    else:
        res = sys.getsizeof(obj)
    return(res)


"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

for i in range(2, 10):
    count = 0
    for y in range(2, 100):
        if (y % i == 0):
            count += 1
    print(f'Числу {i} кратны {count} чисел.')
all_mem = 0
all_mem += size_of(i)
all_mem += size_of(y)
all_mem += size_of(count)
print(f'Суммарное количество паямяти на все объекты = {all_mem}')
"""
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=99
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=11

Суммарное количество паямяти на все объекты = 84

"""


"""

2. Во втором массиве сохранить индексы четных элементов первого массива. Например, 
если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить 
значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. 
именно в этих позициях первого массива стоят четные числа.

"""

N = 10
MAX_EL = 30
MIN_EL = 0
array1 = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]
print(array1)


array2 = []
for i in range(N):
    if (array1[i] % 2 == 0):
        array2.append(i)

print(array2)

count = 0
count += size_of(N)
count += size_of(MAX_EL)
count += size_of(MIN_EL)
count += size_of(array1)
count += size_of(array2)
print(f'Суммарное количество паямяти на все объекты = {count}')
"""
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
type(obj)=<class 'list'>, sys.getsizeof(obj)=184, obj=[15, 29, 17, 18, 2, 2, 0, 18, 1, 20]
type(obj)=<class 'list'>, sys.getsizeof(obj)=120, obj=[3, 4, 5, 6, 7, 9]

Поскольку массив хранит ссылки на объекты, для полного расчета занимаемой памяти посчитаем 
память, занимаемую каждым объектом, на который есть ссылка в массиве и тогда:

Суммарное количество паямяти на все объекты = 468
"""


"""

4. Определить, какое число в массиве встречается чаще всего.

"""

N = 30
MAX_EL = 10
MIN_EL = 0
array = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]
print(array)

uniq = list(set(array))
uniq_count = [0] * len(uniq)
max_count = 0
max_num = 0

for i in range(len(uniq)):
    for j in range(N):
        if (uniq[i] == array[j]):
            uniq_count[i] += 1
            if uniq_count[i] > max_count:
                max_count = uniq_count[i]
                max_num = uniq[i]

print(f'Чаще всего {max_count} раз встречается число {max_num}')
count = 0
count += size_of(N)
count += size_of(MAX_EL)
count += size_of(MIN_EL)
count += size_of(array)
count += size_of(uniq)
count += size_of(uniq_count)
count += size_of(max_num)
count += size_of(i)
count += size_of(j)
print(f'Суммарное количество паямяти на все объекты = {count}')
"""
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
type(obj)=<class 'list'>, sys.getsizeof(obj)=312, obj=[7, 9, 5, 3, 7, 10, 8, 3, 1, 8, 10, 8, 3, 8, 8, 1, 5, 4, 2, 8, 0, 2, 5, 0, 10, 6, 6, 4, 4, 9]
type(obj)=<class 'list'>, sys.getsizeof(obj)=144, obj=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type(obj)=<class 'list'>, sys.getsizeof(obj)=144, obj=[2, 2, 2, 3, 3, 3, 2, 2, 6, 2, 3]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=8
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=29

Аналогично с предыдущей задачей, с учетом объектов внутри массивов:
Суммарное количество паямяти на все объекты = 1492

А теперь попробуем решить последнюю задачу с помощью collections
"""
counter = collections.Counter()
for num in (array):
    counter[num] += 1
print(counter.most_common(1))


count = 0
count += size_of(N)
count += size_of(MAX_EL)
count += size_of(MIN_EL)
count += size_of(array)
count += size_of(counter)
count += size_of(num)

print(f'Суммарное количество паямяти на все объекты = {count}')

"""
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
type(obj)=<class 'list'>, sys.getsizeof(obj)=312, obj=[4, 5, 5, 8, 5, 10, 5, 4, 5, 4, 9, 8, 10, 6, 2, 4, 7, 8, 0, 10, 0, 8, 6, 0, 2, 9, 4, 4, 10, 7]
type(obj)=<class 'collections.Counter'>, sys.getsizeof(obj)=376, obj=Counter({4: 6, 5: 5, 8: 4, 10: 4, 0: 3, 9: 2, 6: 2, 2: 2, 7: 2})
Суммарное количество паямяти на все объекты = 1436


Разница в сумме памяти для хранения внутренних данных исключительно из-за дополнительных переменных
в первом решении, а вот сами объекты хранения этих данных отличаются
В первом случае мы использовали два массива для хранения уникальных чисел и их количеств, это 288 байт,
во втором случае коллекцию, на хранение которой требуется 376 байт
Явный проигрыш по памяти.
Но, что если замерить скорость работы

Скорость первого решения:  1.789322219
Скорость второго решения:  1.005276205

Получаем явный выигрыш не только в лаконичности и красоте кода, но и во времени выполнения
"""


def max_count1(N):
    MAX_EL = 10
    MIN_EL = 0
    array = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]

    uniq = list(set(array))
    uniq_count = [0] * len(uniq)
    max_count = 0
    max_num = 0

    for i in range(len(uniq)):
        for j in range(N):
            if (uniq[i] == array[j]):
                uniq_count[i] += 1
                if uniq_count[i] > max_count:
                    max_count = uniq_count[i]
                    max_num = uniq[i]


def max_count2(N):
    MAX_EL = 10
    MIN_EL = 0
    array = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]

    counter = collections.Counter()
    for num in (array):
        counter[num] += 1


print("Скорость первого решения: ", timeit(
    'max_count1(1000)', number=1000, globals=globals()))
print("Скорость второго решения: ", timeit(
    'max_count2(1000)', number=1000, globals=globals()))
