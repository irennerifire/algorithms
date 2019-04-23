#4. Определить, какое число в массиве встречается чаще всего.

import random as rd

list = [rd.randint(0, 10) for i in range(30)]
print(list)

counter = []

#for i in list:
#    counter.append(list.count(i))

counter = [[el, list.count(el)] for el in set(list)]

#print(f"Количество вхождений каждого числа: {counter}")

maxel = []
for el in counter:
    maxel.append(el[1])

max2 = max(maxel)

max_num = []
for el in counter:
    if el[1] == max2:
        max_num.append(el[0])

print(f"These numbers were met the most of times in the list: {max_num}")



# m=0
# M = []
# for el in counter:
#     if counter.index(el) == 0:
#         pred = el
#     else:
#         if el[1] > pred[1]:
#             m = pred[0]
#         pred = el
#
# print(m)
#
# maxa = max(counter[1])
# print(maxa)
#m_el = counter.index(max(counter))
#print(m_el)
#print(f"Число {list[m_el]} встречается чаще всего ({max(counter)} раз).")
