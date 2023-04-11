import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Introdução aos Layouts')
tela.geometry('600x400')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='red',  # cor do fundo da label
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='blue'  # cor do fundo da label
)

# Layout pack()
label_1.pack(
    side='left',  # lado em que o widget será colocado na tela
    expand=True,  # ocupa por inteiro o espaço disponível na tela para esse widget (eixo X e Y)
    fill='y'  # o widget é preenchido na tela toda ('x' para o eixo X, 'y' para o eixo Y e 'both' para ambos)
)
label_2.pack(
    side='right',
    expand=True,
    fill='both'
)

# Layout grid()
tela.columnconfigure(
    0,  # índice
    weight=1  # tamanho da coluna ocupada na tela
)
tela.columnconfigure(
    1,
    weight=1
)
tela.columnconfigure(
    2,
    weight=2
)
tela.rowconfigure(
    0,
    weight=1,
)
tela.rowconfigure(
    1,
    weight=1,
)
label_1.grid(
    row=0,  # linha a ser colocado o widget
    column=0,  # coluna a ser colocado o widget
    sticky='news'  # informa em qual local do layout o widget estará colocado
)
label_2.grid(
    row=1,
    column=1,
    columnspan=2,  # informar quantas colunas serão ocupadas
    sticky='news'
)

# Layout place()
label_1.place(
    x=100,  # posição no eixo X
    y=200,  # posição no eixo Y
    width=200,  # largura do widget no layout
    height=100  # altura do widget no layout
)
label_2.place(
    relx=0.5,  # posição relativa no eixo X (de 0,0 a 1,0)
    rely=0.5,  # posição relativa no eixo Y (de 0,0 a 1,0)
    relwidth=1,  # largura relativa do widget no layout
    anchor='center'  # o ponto de ancoragem do widget na tela
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
