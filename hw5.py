# + Пользователь вводит данные о количестве предприятий,
# + их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

factory = collections.namedtuple("factory", ["name", "money1", "money2", "money3", "money4"])

col = input("Введите количество Ваших предприятий:      ")

factory_list = []
for i in range(int(col)):
    nam = input("Введите название предприятия:  ")
    first = input("Введите прибыль за 1-ый квартал:     ")
    second = input("Введите прибыль за 2-ый квартал:     ")
    third = input("Введите прибыль за 3-ый квартал:     ")
    fourth = input("Введите прибыль за 4-ый квартал:     ")
    fac = factory(nam, float(first), float(second), float(third), float(fourth))
    factory_list.append(fac)

sum = 0
all_sum = 0
profit = {}
for el in factory_list:
    sum = el.money1 + el.money2 + el.money3 + el.money4
    profit[el.name] = sum
    all_sum += sum

average = all_sum/len(factory_list)
#print(len(factory_list))
print(f" Средняя прибыль за год по всем предприятиям составила: {average} ")

print("Предприятия, чья прибыль за год составила выше среднего значения: ")
for f in profit:
    if profit[f] > average:
        print(f)

print("Предприятия, чья прибыль за год составила ниже среднего значения: ")
for f in profit:
    if profit[f] < average:
        print(f)


#print(factory_list)
