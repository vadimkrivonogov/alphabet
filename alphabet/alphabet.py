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
from math import *
import numpy as np
import matplotlib.pyplot as plt


k=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)

def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=a.get()
    lbl.configure(text=t)
    a.delete(0,END)

def grafik():
    a_=float(a.get())
    b_=float(b.get())
    c_=float(c.get())
    x0=(-b_)/2*a_ 
    y0=a_*x0*x0+b_*x0+c_
    x=np.arange(x0-15,x0+15,1)#min,max
    y=a_*x*x+b_*x+c_
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title('Ruutvõrrand')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()




def Lahenda():
    if a.get()=="": 
        a.configure(bg="red")
    else:
        a.configure(bg="lightblue")
    if b.get()=="": 
        b.configure(bg="red")
    else:
        b.configure(bg="lightblue")
    if c.get()=="": 
        c.configure(bg="red")
    else:
        c.configure(bg="lightblue")
    if a.get()!="" and b.get()!="" and c.get()!="":
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1=round((-b_-sqrt(D))/(2*a_),2)
            x2=round((-b_+sqrt(D))/(2*a_),2)
            vas=f"X1={x1} \nX2={x2}"
        elif D==0:
            x1=round((-1*b_)/(2*a_),2)
            vas=f"X1={x1}"
        else:
            vas="Lahendust pole"
        vastus.configure(text=vas)


aken=Tk()
aken.geometry("650x260")
aken.title("Ruutvõrrandid")
f1=Frame(aken,width=650,height=260)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="Ruutvõrrandite lahendamine",font="Ariel 20", fg="gold",bg="lightblue")
lbl.pack(side=TOP)
vastus=Label(f1,text="Siia tuleb vastus", height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
a=Entry(f1,font="Ariel 20", fg="gold",bg="lightblue",width=3)
a.pack(side=LEFT)
x2=Label(f1,text="x**2+",font="Ariel 20", fg="gold", padx=10)
x2.pack(side=LEFT)
b=Entry(f1,font="Ariel 20", fg="gold",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(f1,text="x+",font="Ariel 20", fg="gold")
x.pack(side=LEFT)
c=Entry(f1,font="Ariel 20", fg="gold",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(f1,text="=0",font="Ariel 20", fg="gold")
y.pack(side=LEFT)
btn=Button(f1,text="Lahenda", font="Ariel 20",bg="gold",command=Lahenda)
btn.pack(side=LEFT)
btn_g=Button(f1,text="Graafik", font="Ariel 20",bg="gold",command=grafik)
btn_g.pack(side=LEFT)

btn_veel=Button(f2,text="Suurendada aken", font="Ariel 20",bg="gold")
btn_veel.pack()


aken.mainloop()
