"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
HEX_NUM = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
DEC_NUM = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def hex_sum(a, b, dop):
    dec_sum = HEX_NUM[a] + HEX_NUM[b] + HEX_NUM[dop]
    in_the_mind = DEC_NUM[dec_sum // 16]
    number = DEC_NUM[dec_sum % 16]
    return([number, in_the_mind])


def hex_mult(a, b, dop):
    dec_sum = HEX_NUM[a] * HEX_NUM[b] + HEX_NUM[dop]
    in_the_mind = DEC_NUM[dec_sum // 16]
    number = DEC_NUM[dec_sum % 16]
    return([number, in_the_mind])


def total_sum(num1, num2):
    num1 = num1.copy()
    num2 = num2.copy()
    summ = collections.deque()
    dop_sum = '0'
    for i in range(max(len(num1), len(num2))):
        a = num1.pop() if len(num1) > 0 else '0'
        b = num2.pop() if len(num2) > 0 else '0'
        res = hex_sum(a, b, dop_sum)
        summ.appendleft(res[0])
        dop_sum = res[1]
    if dop_sum != '0':
        summ.appendleft(dop)
    return(summ)


def total_mult(num1, num2):
    multiply = collections.deque()
    digit = []
    for i in reversed(num1):
        part_mult = collections.deque()
        dop_mult = '0'
        for j in reversed(num2):
            res = hex_mult(i, j, dop_mult)
            part_mult.appendleft(res[0])
            dop_mult = res[1]
        if dop_mult != '0':
            part_mult.appendleft(dop_mult)
        part_mult.extend(digit)
        digit.append('0')
        multiply = total_sum(multiply, part_mult)
    return(multiply)


number1 = list(input("Введите первое число: "))
number2 = list(input("Введите второе число: "))


print(f'Сумма чисел равна: {list(total_sum(number1, number2))}')
print(f'Произведение чисел равно: {list(total_mult(number1, number2))}')
