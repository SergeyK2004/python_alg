'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

Блок-схема: https://drive.google.com/file/d/1QAJPbskewQ6Up0A7NpXXOk-boQTGbFFk/view?usp=sharing
'''

number = int(input('Введите трехзначное число:'))
digit1 = number // 100
number -= digit1 * 100
digit2 = number // 10
digit3 = number - digit2 * 10
print(f'Сумма цифр = {digit1 + digit2 + digit3}')
print(f'Произведение цифр = {digit1 * digit2 * digit3}')
