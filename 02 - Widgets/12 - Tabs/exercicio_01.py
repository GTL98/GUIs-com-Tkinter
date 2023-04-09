# Criar 3 abas e colocar 1 botão, 1 entrada e 1 label em cada uma

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')

# Criar o notebook
notebook = ttk.Notebook(master=tela)

# Criar as abas
aba_1 = ttk.Frame(master=notebook)
aba_2 = ttk.Frame(master=notebook)
aba_3 = ttk.Frame(master=notebook)

# Colocar os widgets na Aba 1
botao_1 = ttk.Button(
    master=aba_1,
    text='Botão da Aba 1'
)
entrada_1 = ttk.Entry(master=aba_1)
label_1 = ttk.Label(
    master=aba_1,
    text='Label da Aba 1'
)
botao_1.pack()
entrada_1.pack()
label_1.pack()

# Colocar os widgets na Aba 2
botao_2 = ttk.Button(
    master=aba_2,
    text='Botão da Aba 2'
)
entrada_2 = ttk.Entry(master=aba_2)
label_2 = ttk.Label(
    master=aba_2,
    text='Label da Aba 2'
)
botao_2.pack()
entrada_2.pack()
label_2.pack()

# Colocar os widgets na Aba 3
botao_3 = ttk.Button(
    master=aba_3,
    text='Botão da Aba 3'
)
entrada_3 = ttk.Entry(master=aba_3)
label_3 = ttk.Label(
    master=aba_3,
    text='Label da Aba 3'
)
botao_3.pack()
entrada_3.pack()
label_3.pack()

# Adicionar as abas no notebook
notebook.add(
    aba_1,
    text='Aba 1'
)
notebook.add(
    aba_2,
    text='Aba 2'
)
notebook.add(
    aba_3,
    text='Aba 3'
)
notebook.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
