'''
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

Блок-схема: https://drive.google.com/file/d/1pJDNUmgx8z5zdXT-0ImWu2lNUiZ66tvN/view?usp=sharing
'''
n = int(input('Введите n для проверки равенства: '))
sum = 0
for i in range(1, n+1):
    sum += i
rezult = n * (n + 1) / 2
if rezult == sum:
    print(f'Равенство верно, результат: {sum} = {rezult}')
else:
    print(f'Равенство неверно, результат: {sum} = {rezult}')
