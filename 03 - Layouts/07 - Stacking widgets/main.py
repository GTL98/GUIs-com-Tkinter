import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Sobreposição de widgets')
tela.geometry('400x400')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='green'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='red'
)

label_1.lift()  # permite que o widget fique acima de outro, independente da ordem de criação do widget
label_2.lower()  # pertmite que o widget fique abaixo de outro, indepdendente da ordem de criação do widget

botao_1 = ttk.Button(
    master=tela,
    text='Botão Label 1',
    command=lambda: label_1.lift()  # .tkraise() funciona igual
)
botao_2 = ttk.Button(
    master=tela,
    text='Botão Label 2',
    command=lambda: label_2.tkraise()
)

# Layout
label_1.place(
    x=50,
    y=100,
    width=200,
    height=150
)
label_2.place(
    x=150,
    y=60,
    width=140,
    height=100
)

botao_1.place(
    relx=0.8,
    rely=1,
    anchor='se'
)
botao_2.place(
    relx=1,
    rely=1,
    anchor='se'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
