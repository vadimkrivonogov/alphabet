# Словарь для русского алфавита
rus_alphabet = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9,
    'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18,
    'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27,
    'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33
}

# Словарь для латинского алфавита
eng_alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

# Запрос имени у пользователя
name = input("Введите ваше имя: ")

# Определение алфавита
if set(name.lower()).issubset(set(rus_alphabet.keys())):
    alphabet = rus_alphabet
elif set(name.lower()).issubset(set(eng_alphabet.keys())):
    alphabet = eng_alphabet
else:
    print("Не удалось определить алфавит")
    exit()

# Расчет числа имени
name_number = sum([alphabet[char.lower()] for char in name if char.lower() in alphabet])

# Сведение числа к однозначному числу
while name_number > 9:
    name_number = sum([int(digit) for digit in str(name_number)])

# Вывод результата
print(f"Число вашего имени: {name_number}")
