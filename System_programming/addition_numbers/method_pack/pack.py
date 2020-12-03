from tkinter import *

root = Tk()
f_top = Frame (root)
lab = Label (width=15)
e1 = Entry(text='Код цвета', width=15)
e1.insert(0, 'Код цвета')
lab['text'] = 'Цвет'

def insert():
    e1.delete(0, END)
    e1.insert(0, "#ff0000")
    lab['text'] = 'Красный'
def insert2():
    e1.delete(0, END)
    e1.insert(0, "#ffa500")
    lab['text'] = 'Оранжевый'
def insert3():
    e1.delete(0, END)
    e1.insert(0, "#ffff00")
    lab['text'] = 'Жёлтый'
def insert4():
    e1.delete(0, END)
    e1.insert(0, "#00ff00")
    lab['text'] = 'Зелёный'
def insert5():
    e1.delete(0, END)
    e1.insert(0, "#00ffff")
    lab['text'] = 'Голубой'
def insert6():
    e1.delete(0, END)
    e1.insert(0, "#0000ff")
    lab['text'] = 'Синий'
def insert7():
    e1.delete(0, END)
    e1.insert(0, "#800080")
    lab['text'] = 'Фиолетовый'


b = Button(bg = '#ff0000', command = insert, width=3)
b2 = Button(bg = '#FFA500', command = insert2, width = 3)
b3 = Button(bg = '#FFFF00', command = insert3, width = 3)
b4 = Button(bg = '#00FF00', command = insert4, width = 3)
b5 = Button(bg = '#00FFFF', command = insert5, width = 3)
b6 = Button(bg = '#0000FF', command = insert6, width = 3)
b7 = Button(bg = '#800080', command = insert7, width = 3)

lab.pack(padx = 2, pady = 2)
e1.pack(padx = 2, pady = 2)
f_top.pack(padx = 2, pady = 2)
b.pack(side = LEFT, padx= 1, pady = 5)
b2.pack(side = LEFT, padx = 1, pady = 5)
b3.pack(side = LEFT, padx = 1, pady = 5)
b4.pack(side = LEFT, padx = 1, pady = 5)
b5.pack(side = LEFT, padx = 1, pady = 5)
b6.pack(side = LEFT, padx = 1, pady = 5)
b7.pack(side = LEFT, padx = 1, pady = 5)

root.mainloop()