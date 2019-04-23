# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list1 = [i for i in range(2, 100)] #нет уточнения - 99 включая или нет
print(list1)

list2 = [i for i in range(2, 10)] #аналогично нет уточнения
print(list2)

count = 0
for el1 in list1:
    for el2 in list2:
        if el1 % el2 == 0:
            count += 1

print(count)
