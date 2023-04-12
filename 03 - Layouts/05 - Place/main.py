import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Place Layout')
tela.geometry('400x600')

# Widgets
label_1 = ttk.Label(
    master=tela,
    text='Label 1',
    background='red'
)
label_2 = ttk.Label(
    master=tela,
    text='Label 2',
    background='blue'
)
label_3 = ttk.Label(
    master=tela,
    text='Label 3',
    background='green'
)
botao = ttk.Button(
    master=tela,
    text='Botão 1'
)

# Layout
label_1.place(
    # Posição absoluta: informar a posição dos pixels, não acompanha a redimensionalidade da tela
    x=300,  # posição no eixo X em pixels
    y=100,  # posição no eixo Y wm pixels
    width=100,  # largura do widget em pixels
    height=200  # altura do widget em pixels
)
label_2.place(
    # Posição relativa: informar a posição em forma de porcentagem, acompanha a redimensionalidade da tela
    relx=0.2,  # posição relativa no eixo X (valores entre 0 e 1)
    rely=0.1,  # posição relativa no eixo Y (valores entre 0 e 1)
    relwidth=0.4,  # largura relativa do widget (valores entre 0 e 1)
    relheight=0.5  # altura relativa do widget (valores entre 0 e 1)
)
label_3.place(
    x=80,
    y=60,
    width=160,
    height=300
)
botao.place(
    relx=1,
    rely=1,
    anchor='se'  # indica onde será a ancoragem do widget na tela
)

# Frame
frame = ttk.Frame(master=tela)
frame_label = ttk.Label(
    master=frame,
    text='Label Frame',
    background='yellow'
)
frame_botao = ttk.Button(
    master=frame,
    text='Botão Frame',
)

# Frame Layout
frame.place(
    relx=0,
    rely=0,
    relwidth=0.3,
    relheight=1
)
frame_label.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=0.5
)
frame_botao.place(
    relx=0,
    rely=0.5,
    relwidth=1,
    relheight=0.5
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
