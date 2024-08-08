import tkinter as tk

pencere = tk.Tk()
pencere.title('Hesap Makinesi')
pencere.geometry('200x200')
label = tk.Label(pencere, text='Hosgeldin islem iceren butona bas')
label.pack()

entry = tk.Entry(pencere)
entry2 = tk.Entry(pencere)
entry.pack()
entry2.pack()
def topla():
    sonuc = int(entry.get()) + int(entry2.get())
    label.config(text=sonuc)

def Cikart():
    sonuc = int(entry.get()) - int(entry2.get())
    label.config(text=sonuc)

def Carp():
    sonuc = int(entry.get()) * int(entry2.get())
    label.config(text=sonuc)

def Bol():
    sonuc = int(entry.get()) / int(entry2.get())
    label.config(text=sonuc)

buton = tk.Button(pencere, text=' + ', command=topla)
buton2 = tk.Button(pencere, text=' - ', command=Cikart)
buton3 = tk.Button(pencere, text=' * ', command=Carp)
buton4 = tk.Button(pencere, text=' / ', command=Bol)
buton.pack()
buton2.pack()
buton3.pack()
buton4.pack()

pencere.mainloop()