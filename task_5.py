"""

5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.

"""
import random

N = 10
MAX_EL = 10
MIN_EL = -10
array = [random.randint(MIN_EL, MAX_EL) for _ in range(N)]
print(array)
max_index = -1
for i in range(N):
    if array[i] < 0:
        if max_index == -1:
            max_index = i
        elif (array[i] > array[max_index]):
            max_index = i
if max_index == -1:
    print('Отрицательных чисел в массиве не найдено.')
else:
    print(f'Максимальное отрицательное число = {array[max_index]} \
и его индекс в массиве = {max_index}')
