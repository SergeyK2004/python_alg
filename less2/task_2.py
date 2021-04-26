'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

Блок-схема: https://drive.google.com/file/d/1pJDNUmgx8z5zdXT-0ImWu2lNUiZ66tvN/view?usp=sharing
'''
num = int(input('Введите число: '))
odd = ''
even = ''
while num > 0:
    digit = num % 10
    num = num // 10
    if (digit % 2 == 0):
        even = even + str(digit) + ','
    else:
        odd = odd + str(digit) + ','
print(f'Четные цифры: {even}')
print(f'Количество четных: {len(even)}')
print(f'Нечетные цифры: {odd}')
print(f'Количество нечетных: {len(odd)}')
