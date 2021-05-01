"""

4. Определить, какое число в массиве встречается чаще всего.

"""
import random

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
