import tkinter as tk
import pygame
import random
import threading
import time


def flashing():  # задаем функцию переливания кнопки
    while True:
        btn.config(bg='red')
        time.sleep(0.05)
        btn.config(bg='orange')
        time.sleep(0.05)
        btn.config(bg='yellow')
        time.sleep(0.05)
        btn.config(bg='green')
        time.sleep(0.05)
        btn.config(bg='lightblue')
        time.sleep(0.05)
        btn.config(bg='blue')
        time.sleep(0.05)
        btn.config(bg='purple')
        time.sleep(0.05)


def getkey():  # задаем функцию для генерации ключа
    key = 'Key:'
    one = ''
    two = ''
    three = ''
    word = [i for i in arg_ent.get()]  # достаем слово из ввода пользователя и преобразуем в список
    letters = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']  # список всех заглавных букв алфавита
    letterslow = [b for b in 'abcdefghijklmnopqrstuvwxyz']  # список всех строчных букв алфавита
    if len(word) != 6 or any(a in word for a in letterslow):  # ограничиваем ввод 6-ю заглавными буквами
        keygen.configure(text=key + 'WRONG INPUT')  # в случае ввода с нижним регистром или слова не из букв
    else:
        for first in range(3):
            a = str(random.choice(word))
            one = one + a
        for second in range(6):
            b = str((letters.index(random.choice(word)) + 1) % 10)
            two = two + b
        for third in range(3):
            c = str(random.choice(word))
            three = three + c
        keygen.configure(text=key + one + '-' + two + '-' + three)


# задаем сам tkinter, разрешение его окна

window = tk.Tk()
window.title('NFS UNBOUND KEYGEN')
window.geometry('1280x720')

# фон из игры

bg = tk.PhotoImage(file='NFS.png')
lbl_bg = tk.Label(image=bg)
lbl_bg.place(x=0, y=0)

# описание задачи пользователя

lbl_ent = tk.Label(text='Enter 6 letters word, only caps', bg='#ffffff', fg='#009900', font=('panton black', 30))
lbl_ent.place(x=350, y=50)

# поле для ввода 6-буквенного слова

arg_ent = tk.Entry(width=10)
arg_ent.insert(0, '')
arg_ent.place(x=580, y=150)

# кнопка для генерации ключа

btn = tk.Button(window, text="generate", command=getkey)
btn.pack()
btn.place(x=584, y=200)
threading.Thread(target=flashing, args=[], daemon=True).start()  # переливание кнопки

# окошко с выводом ключа

keygen = tk.Label(text='Key:', bg='#ffffff', fg='#000000', font=('panton', 10))
keygen.place(x=540, y=250)

# добавляем музыку

music = "NFS.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()

window.mainloop()
