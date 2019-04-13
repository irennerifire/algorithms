#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
ch = input("Выберите алфавит: 1 - русский, 2 - английский:  ")
a = input("Укажите номер буквы в алфавите:   ")
alph_en = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alph_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

if ch == "1":
    letter = alph_ru[int(a)]
    print(f"Это буква {letter}")
elif ch == "2":
    letter = alph_en[int(a)]
    print(f"Это буква {letter}")
