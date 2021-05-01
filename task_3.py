"""

3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""
import random

N = 30
MAX_EL = 20
MIN_EL = 0
array = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]
print(array)

min_index = 0
max_index = 0
for i in range(N):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i
print(f'Меняем местами {min_index} и {max_index} элементы')
num = array[min_index]
array[min_index] = array[max_index]
array[max_index] = num
print(array)
