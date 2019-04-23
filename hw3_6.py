# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random as rd

list = [rd.randint(0, 100) for i in range(15)]
print(list)

max_el = max(list)
min_el = min(list)

sum = 0
print(range(list.index(min_el), list.index(max_el)))

if list.index(min_el) < list.index(max_el):
    for i in range(list.index(min_el)+1, list.index(max_el)):
        sum += list[i]
else:
    for i in range(list.index(max_el)+1, list.index(min_el)):
        sum += list[i]

print(f"Max element = {max_el}, min element = {min_el}")
print(f"The sum of numbers between them = {sum}")
