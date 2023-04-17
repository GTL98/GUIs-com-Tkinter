import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Layouts Combinados')
tela.geometry('600x600')
tela.minsize(600, 600)

# Widgets do layout principal
frame_menu = ttk.Frame(master=tela)
frame_principal = ttk.Frame(master=tela)

# Layout place() principal
frame_menu.place(
    x=0,
    y=0,
    relwidth=0.3,
    relheight=1
)
frame_principal.place(
    relx=0.3,
    y=0,
    relwidth=0.7,
    relheight=1
)

# Wigets do menu
botao_menu_1 = ttk.Button(
    master=frame_menu,
    text='Botão 1'
)
botao_menu_2 = ttk.Button(
    master=frame_menu,
    text='Botão 2'
)
botao_menu_3 = ttk.Button(
    master=frame_menu,
    text='Botão 3'
)

slider_menu_1 = ttk.Scale(
    master=frame_menu,
    orient='vertical'
)
slider_menu_2 = ttk.Scale(
    master=frame_menu,
    orient='vertical'
)

frame_alternar = ttk.Frame(master=frame_menu)
menu_alternar_1 = ttk.Checkbutton(
    frame_alternar,
    text='Check 1'
)
menu_alternar_2 = ttk.Checkbutton(
    frame_alternar,
    text='Check 2'
)

entrada = ttk.Entry(master=frame_menu)

# Layout do menu
frame_menu.columnconfigure(
    index=(0, 1, 2),
    weight=1,
    uniform='a'
)
frame_menu.rowconfigure(
    index=(0, 1, 2, 3, 4),
    weight=1,
    uniform='a'
)

botao_menu_1.grid(
    column=0,
    row=0,
    sticky='news',
    columnspan=2
)
botao_menu_2.grid(
    column=2,
    row=0,
    sticky='news',
)
botao_menu_3.grid(
    column=0,
    row=1,
    sticky='news',
    columnspan=3
)

slider_menu_1.grid(
    column=0,
    row=2,
    sticky='news',
    rowspan=2,
    pady=20
)
slider_menu_2.grid(
    column=2,
    row=2,
    sticky='news',
    rowspan=2,
    pady=20
)

# Layout alternar
frame_alternar.grid(
    column=0,
    row=4,
    columnspan=3,
    sticky='news'
)
menu_alternar_1.pack(
    side='left',
    expand=True
)
menu_alternar_2.pack(
    side='left',
    expand=True
)

# Layout entrada
entrada.place(
    relx=0.5,
    rely=0.95,
    relwidth=0.9,
    anchor='center'
)

# Widgets do menu principal
frame_entrada_1 = ttk.Frame(master=frame_principal)
label_principal_1 = ttk.Label(
    master=frame_entrada_1,
    text='Label 1',
    background='red'
)
botao_principal_1 = ttk.Button(
    master=frame_entrada_1,
    text='Botão 1'
)

frame_entrada_2 = ttk.Frame(master=frame_principal)
label_principal_2 = ttk.Label(
    master=frame_entrada_2,
    text='Label 2',
    background='blue'
)
botao_principal_2 = ttk.Button(
    master=frame_entrada_2,
    text='Botão 2'
)

# Layout principal
frame_entrada_1.pack(
    side='left',
    expand=True,
    fill='both',
    padx=20,
    pady=20
)
frame_entrada_2.pack(
    side='left',
    expand=True,
    fill='both',
    padx=20,
    pady=20
)

label_principal_1.pack(
    expand=True,
    fill='both'
)
botao_principal_1.pack(
    expand=True,
    fill='both',
    pady=10
)

label_principal_2.pack(
    expand=True,
    fill='both'
)
botao_principal_2.pack(
    expand=True,
    fill='both',
    pady=10
)

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
