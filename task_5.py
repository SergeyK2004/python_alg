'''
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

Блок-схема: https://drive.google.com/file/d/1QAJPbskewQ6Up0A7NpXXOk-boQTGbFFk/view?usp=sharing
'''
letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')

number1 = ord(letter1) - 96
number2 = ord(letter2) - 96

if number2 > number1:
    count = number2 - number1 - 1
    print(f'Буква {letter1} это {number1} буква алфавита')
    print(f'Буква {letter2} это {number2} буква алфавита')

    if count == 0:
        print('Это соседние буквы, между ними ничего нет.')
    else:
        print(f'Между ними есть {count} букв')
else:
    print('Буквы заданы неверно.')
