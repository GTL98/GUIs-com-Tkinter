# Criar uma barra de progresso vertical que inicia automaticamente e mostra o progresso como
# um número. Criar também um slider que interfere na barra de progresso

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')

# Variáveis
var_int = tk.IntVar()

# Barra de progresso
progresso = ttk.Progressbar(
    master=tela,
    variable=var_int,
    maximum=100,
    orient='vertical'
)
progresso.pack()
progresso.start()

# Slider
slider = ttk.Scale(
    master=tela,
    variable=var_int,
    from_=0,
    to=100
)
slider.pack()

# Label
label = ttk.Label(
    master=tela,
    textvariable=var_int
)
label.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
