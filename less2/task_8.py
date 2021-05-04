'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

Блок-схема: https://drive.google.com/file/d/1pJDNUmgx8z5zdXT-0ImWu2lNUiZ66tvN/view?usp=sharing
'''
quantity = int(input('Укажите количество вводимых чисел: '))
digit = input('Введите цифру для поиска: ')
sum = 0
for i in range(1, quantity+1):
    number = input(f'Введите {i}-е число: ')
    sum += number.count(digit)
print(f'Количество цифр {digit} в введенных числах = {sum}')
