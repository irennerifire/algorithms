# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random as rd

list1 = [rd.randint(0, 500) for i in range(15)]
print(list1)

list2 = []

for el in list1:
    if el % 2 == 0:
        list2.append(list1.index(el))

print(list2)
