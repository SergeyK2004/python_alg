"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и 
отдельно вывести наименования предприятий, чья прибыль ниже среднего.

"""
import collections
companys = {}
n = int(input("Количество компаний: "))
profit = collections.Counter()
for i in range(n):
    company_profit = 0
    company_name = input(f'Название {str(i+1)}-й компании: ')
    for j in range(4):
        company_profit += int(input(f'Прибыль за {str(j+1)}-й месяц: '))
    companys[company_name] = collections.Counter(prof=company_profit)
    profit += companys[company_name]

average = profit["prof"] / n
print(f'\nСредняя прибыль: {average}')
print("Предприятия с прибылью выше среднего:")
for i in companys:
    if companys[i]["prof"] > average:
        print(i)
print("-" * 30)
print("Предприятия с прибылью ниже среднего:")
for i in companys:
    if companys[i]["prof"] < average:
        print(i)
