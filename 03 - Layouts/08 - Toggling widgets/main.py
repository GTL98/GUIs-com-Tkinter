import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Esconder Widgets')
tela.geometry('600x400')


# Layout place()
def alterar_label_place():
    """Função responsável por altenar a posição da label
    no layout place() quando o botão foi acionado."""
    global label_visivel

    if label_visivel:
        label.place_forget()
        label_visivel = False
    else:
        label_visivel = True
        label.place(
            relx=0.5,
            rely=0.5,
            anchor='center'
        )


botao = ttk.Button(
    master=tela,
    text='Alternar Label',
    command=alterar_label_place
)
botao.place(
    x=10,
    y=10
)

label_visivel = True  # uma flag para garantir que a Label desaparecerá e reaparecerá sempre que o botão for acionado
label = ttk.Label(
    master=tela,
    text='Uma Label'
)
label.place(
    relx=0.5,
    rely=0.5,
    anchor='center'
)


# Layout grid()
def alterar_label_grid():
    """Função responsável por altenar a posição da label
        no layout grid() quando o botão foi acionado."""
    global label_visivel

    if label_visivel:
        label.grid_forget()
        label_visivel = False
    else:
        label_visivel = True
        label.grid(
            column=1,
            row=0
        )


tela.columnconfigure(
    index=(0, 1),
    weight=1,
    uniform='a'
)
tela.rowconfigure(
    index=0,
    weight=1,
    uniform='a'
)
botao = ttk.Button(
    master=tela,
    text='Alternar Label',
    command=alterar_label_grid
)
botao.grid(
    column=0,
    row=0
)

label_visivel = True
label = ttk.Label(
    master=tela,
    text='Uma Label'
)
label.grid(
    column=1,
    row=0
)


# Layout pack()
def alterar_label_pack():
    """Função responsável por altenar a posição da label
    no layout pack() quando o botão foi acionado."""
    global label_visivel

    if label_visivel:
        label.pack_forget()
        label_visivel = False
        frame.pack(
            expand=True,
            before=botao  # esse parâmetro indica que esse widget será colocado antes do widget desejado
        )
    else:
        frame.pack_forget()
        label.pack(
            expand=True,
            before=botao
        )
        label_visivel = True


label_visivel = True
label = ttk.Label(
    master=tela,
    text='Uma Label'
)
label.pack(expand=True)

botao = ttk.Button(
    master=tela,
    text='Alternar Label',
    command=alterar_label_pack
)
botao.pack()

frame = ttk.Frame(master=tela)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
