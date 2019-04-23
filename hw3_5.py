#5. В массиве найти максимальный отрицательный элемент.
#Вывести на экран его значение и позицию в массиве.

import random as rd

list = [rd.randint(-100, 100) for i in range(15)]
print(list)

N = -1

for i in list:
    if i < 0:
        if N == -1:
            N = list.index(i)
        else:
            if abs(i) > abs(list[N]):
                N = list.index(i)

if N != -1:
    print("There some negative numbers in the list")
    print(f"The maximal negative number is the number {list[N]} with index {N}")
