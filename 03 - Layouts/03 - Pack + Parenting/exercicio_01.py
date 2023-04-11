# Criar mais um frame:
    # Ele deve conter 3 botões;
    # Os botões devem estar na vertical e;
    # Esse frame deve estar dentro do "frame_baixo" do arquivo main.py

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('400x600')

# Frame de cima
frame_cima = ttk.Frame(master=tela)
label_1 = ttk.Label(
    master=frame_cima,
    text='Primeira Label',
    background='red'
)
label_2 = ttk.Label(
    master=frame_cima,
    text='Label 2',
    background='blue'
)

# Widget central
label_3 = ttk.Label(
    master=tela,
    text='Outra Label',
    background='green'
)

# Frame de baixo
frame_baixo = ttk.Frame(master=tela)
label_4 = ttk.Label(
    master=frame_baixo,
    text='Última Label das Labels',
    background='orange'
)
botao_1 = ttk.Button(
    master=frame_baixo,
    text='Um Botão'
)
botao_2 = ttk.Button(
    master=frame_baixo,
    text='Outro Botão'
)

# Frame interno
frame_interno = ttk.Frame(master=frame_baixo)
botao_3 = ttk.Button(
    master=frame_interno,
    text='Botão 3'
)
botao_4 = ttk.Button(
    master=frame_interno,
    text='Botão 4'
)
botao_5 = ttk.Button(
    master=frame_interno,
    text='Botão 5'
)

# Layout de cima
label_1.pack(
    side='left',
    fill='both',
    expand=True
)
label_2.pack(
    side='left',
    fill='both',
    expand=True
)
frame_cima.pack(
    fill='both',
    expand=True
)

# Layout central
label_3.pack(expand=True)

# Layout de baixo
botao_1.pack(
    side='left',
    expand=True,
    fill='both'
)
label_4.pack(
    side='left',
    expand=True,
    fill='both'
)
botao_2.pack(
    side='left',
    expand=True,
    fill='both'
)
frame_baixo.pack(
    expand=True,
    fill='both',
    padx=20,
    pady=20
)

# Frame interno
botao_3.pack(
    expand=True,
    fill='both'
)
botao_4.pack(
    expand=True,
    fill='both'
)
botao_5.pack(
    expand=True,
    fill='both'
)
frame_interno.pack(
    side='left',
    expand=True,
    fill='both'
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
