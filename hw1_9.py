#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
num1 = float(input("Enter 1 number      "))
num2 = float(input("Enter 2 number      "))
num3 = float(input("Enter 3 number      "))

list = [num1, num2, num3]

maxn = max(list)
minn = min(list)

for i in list:
    if i != maxn and i !=minn:
        print(f"The middle number is: {i}")
