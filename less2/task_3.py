'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

Блок-схема: https://drive.google.com/file/d/1pJDNUmgx8z5zdXT-0ImWu2lNUiZ66tvN/view?usp=sharing
'''


def func(a):
    if a > 10:
        b = a % 10
        a = a // 10
        return (f'{b}{func(a)}')
    return (f'{a}')


num = int(input('Введите число: '))
new_num = func(num)
print(f'Обратное число: {new_num}')
