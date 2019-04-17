# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

colnum = int(input("Введите количество чисел, которые будут исследоваться:  "))
nat_nums = []

print("Введите натуральные числа через enter")
for i in range(colnum):
    nat_nums.append(input())

sums = []
sum =0

for el in nat_nums:
    for j in el:
        sum += int(j)
    sums.append(sum)
    sum = 0

#print(sums)
m = max(sums)
print(f"Максимальная сумма цифр составила: {m}. Она относится к числу {nat_nums[sums.index(m)]}")
