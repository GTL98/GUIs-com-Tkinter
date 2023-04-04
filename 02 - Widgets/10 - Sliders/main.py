import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # é um conjunto de widgets

# Tela
tela = tk.Tk()
tela.title('Sliders')

# Slider
escala_float = tk.DoubleVar(value=15)
escala = ttk.Scale(
    master=tela,
    command=lambda valor: progresso.stop(),
    from_=0,  # valor mínimo
    to=25,  # valor máximo
    length=300,  # dimensão da barra
    orient='vertical',  # orientação da barra
    variable=escala_float
)
escala.pack()

# Barra de progresso
progresso = ttk.Progressbar(
    master=tela,
    variable=escala_float,
    maximum=25,  # valor máximo da barra de progresso
    orient='horizontal',
    mode='indeterminate',  # "determinate" para a barra contínua e "indeterminate" para um quadrado somente
    length=400
)
progresso.pack()

# Navegar pelo texto
texto_navegavel = scrolledtext.ScrolledText(
    master=tela,
    width=100,
    height=5
)
texto_navegavel.pack()

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
