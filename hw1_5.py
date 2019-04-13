#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
a = input("Укажите 2 любые буквы:   ")
alph = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

index = []

for num, el in enumerate(alph):
    for i in a:
        if el == i:
            index.append(num)

distance = index[-1] - index[0]
print(f"Буквы {a} находятся на местах с индексами {index}")
print(f"Между ними {distance} букв")
print(len(alph))
