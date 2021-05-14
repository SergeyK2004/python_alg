"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу
можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках

"""
import random

MAX_EL = 50
MIN_EL = 0
NUMBER_M = 15
array = [random.randint(MIN_EL, MAX_EL) for _ in range(NUMBER_M * 2 + 1)]
for i in range(len(array)):
    median = array[i]
    count_less = count_more = count_equally = 0
    for j in range(len(array)):
        if array[j] > median:
            count_more += 1
        elif array[j] < median:
            count_less += 1
        else:
            count_equally += 1
    if abs(count_less - count_more) < count_equally:
        break


print(array)
print(f'Медиана массива - число {median}')
print('Проведем проверку через сортировку массива')
sort_arr = sorted(array)
print(f'Отсориторованный массив \n{sort_arr}')
print(f'Медиана это {int((len(sort_arr) + 1) / 2)}-й элемент, он равен: {sort_arr[int((len(array) - 1) / 2)]}')