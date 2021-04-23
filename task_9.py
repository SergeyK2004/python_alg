'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

Эту задачу я доделывал после вебинара, поэтому написал другое решение, отличное от показанного вами
С двойной проверкой нагляднее, что мы ищем среднее, но не интересно самому дописывать то, что уже показали.

Блок-схема: https://drive.google.com/file/d/1QAJPbskewQ6Up0A7NpXXOk-boQTGbFFk/view?usp=sharing
'''
print('Введите три числа: ')
a = int(input('1-e: '))
b = int(input('2-e: '))
c = int(input('3-e: '))

if (a == max(a, b, c)) or (a == min(a, b, c)):
    if (b == max(a, b, c)) or (b == min(a, b, c)):
        print(f'Среднее: {c}')
    else:
        print(f'Среднее: {b}')
else:
    print(f'Среднее: {a}')
