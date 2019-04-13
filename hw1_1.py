#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = input("Enter some numerical value of 3 digits:    ")

sum = 0
prod = 1

for i in num:
    sum += int(i)
    prod *= int(i)

print(f"Sum of digits:  {sum}")
print(f"Production of digits: {prod}")
