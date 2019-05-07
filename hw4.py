#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import timeit

def for_cycle():
    #num = input("Enter some numerical value of 3 digits:    ")
    num = "456"
    sum = 0
    prod = 1
    for i in num:
        sum += int(i)
        prod *= int(i)
    return(sum, prod)

def while_cycle():
    #num = input("Enter some numerical value of 3 digits:    ")
    num = "456"
    sum = 0
    prod = 1
    i = 0
    while i < len(num):
        sum = sum + int(num[i])
        prod = prod * int(num[i])
        i += 1
    return(sum, prod)

#print(for_cycle(num))
#print(while_cycle(num))

print(timeit.timeit("for_cycle()", setup="from __main__ import for_cycle", number = 10000))
print(timeit.timeit("while_cycle()", setup="from __main__ import while_cycle", number = 10000))
#Отрабатывает за 0.04947942 и 0.06230678199999999 соответственно

print(timeit.timeit("for_cycle()", setup="from __main__ import for_cycle", number = 100000))
print(timeit.timeit("while_cycle()", setup="from __main__ import while_cycle", number = 100000))
#Отрабатывает за 0.062519189 и 0.08351582599999999 соответственно

print(timeit.timeit("for_cycle()", setup="from __main__ import for_cycle", number = 1000000))
print(timeit.timeit("while_cycle()", setup="from __main__ import while_cycle", number = 1000000))
#Отрабатывает за 0.671649856 и 5.030848927 соответственно

#Видим, что преимущество цикла for сказывается на особенно объемных вычислениях,
#если запустить программу 1 раз, преимущество очевидно не будет.
