# Criar uma label e colocá-la no centro a direita da tela
# A label deve ter metade da largura da tela e 200px de altura

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('400x600')

# Label
label = ttk.Label(
    master=tela,
    text='Uma Label para o exercício',
    background='red'
)

# Layout
label.place(
    relx=1,
    rely=0.5,
    anchor='se',
    relwidth=0.5,
    height=200
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
