'''
По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.

Блок-схема: https://drive.google.com/file/d/1QAJPbskewQ6Up0A7NpXXOk-boQTGbFFk/view?usp=sharing
'''


def formatNumber(n): return n if n % 1 else int(n)


x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))

x_del = x2 - x1
y_del = y2 - y1
k = formatNumber(y_del / x_del)

d = formatNumber(-(y_del * x1 / x_del) + y1)

if d < 0:
    print(f'Уравнение прямой: Y = {k}X - {abs(d)}')
elif d == 0:
    print(f'Уравнение прямой: Y = {k}X')
else:
    print(f'Уравнение прямой: Y = {k}X + {d}')
