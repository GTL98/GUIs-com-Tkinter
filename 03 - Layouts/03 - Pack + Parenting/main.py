import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Pack + Frames')
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

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
