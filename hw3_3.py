# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rd

list1 = [rd.randint(0, 500) for i in range(15)]
print(list1)

max_el = max(list1)
min_el = min(list1)

max_el_index = list1.index(max_el)
min_el_index = list1.index(min_el)

print(f"Max element: {max_el}, min element: {min_el}")

list1[max_el_index] = min_el
list1[min_el_index] = max_el

print(list1)
