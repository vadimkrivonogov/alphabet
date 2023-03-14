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


from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# функция для решения квадратного уравнения
def solve_quadratic():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    
    if a == 0:
        result_label.config(text="Ошибка: a не должно быть равно нулю", fg="red")
        return
    
    D = b*b - 4*a*c
    
    if D < 0:
        result_label.config(text="Нет действительных корней", fg="red")
        return
    elif D == 0:
        x = -b / (2*a)
        result_label.config(text=f"Уравнение имеет один корень: x={x}", fg="green")
    else:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        result_label.config(text=f"Корни уравнения: x1={x1}, x2={x2}", fg="green")

# функция для построения графика квадратичной функции
def plot_graph():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    
    x = np.linspace(-10, 10, 1000)
    y = a*x*x + b*x + c
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Квадратичная функция')
    plt.grid(True)
    plt.show()

# создание окна
root = Tk()
root.title("Решение квадратного уравнения")

# создание элементов интерфейса
a_label = Label(root, text="a")
a_label.grid(row=0, column=0)

a_entry = Entry(root)
a_entry.grid(row=0, column=1)

b_label = Label(root, text="b")
b_label.grid(row=1, column=0)

b_entry = Entry(root)
b_entry.grid(row=1, column=1)

c_label = Label(root, text="c")
c_label.grid(row=2, column=0)

c_entry = Entry(root)
c_entry.grid(row=2, column=1)

solve_button = Button(root, text="Решить", command=solve_quadratic)
solve_button.grid(row=3, column=0)

plot_button = Button(root, text="Построить график", command=plot_graph)
plot_button.grid(row=3, column=1)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# запуск окна
root.mainloop()
