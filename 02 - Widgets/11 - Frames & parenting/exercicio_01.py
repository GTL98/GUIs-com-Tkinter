# Crie um frame com uma label, um botão e uma entrada e
# o coloque do lado direito da tela

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('600x400')

# Frame
frame = ttk.Frame(
    master=tela,
    width=200,
    height=100,
    borderwidth=1,
    relief=tk.GROOVE
)
frame.pack(side='right')

# Label
label = ttk.Label(
    master=frame,
    text='Isso é uma label'
)
label.pack()

# Botão
botao = ttk.Button(
    master=frame,
    text='Isso é um botão'
)
botao.pack()

# Entrada
entrada = ttk.Entry(master=frame)
entrada.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
