import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Menu')
tela.geometry('600x400')

# Menu principal
menu = tk.Menu(master=tela)
tela.configure(menu=menu)  # não deve-se utilizar pack() com o widget Menu()

# Criar o submenu de arquivo
menu_arquivo = tk.Menu(
    master=menu,
    tearoff=False  # impede que uma nova janela seja criada só para o submenu
)

# Colocar entradas no submenu de arquivo
menu_arquivo.add_command(
    label='Novo',
    command=lambda: print('Novo arquivo')
)
menu_arquivo.add_command(
    label='Abrir',
    command=lambda: print('Abrir arquivo')
)

# Criar o submenu de ajuda
menu_ajuda = tk.Menu(
    master=menu,
    tearoff=False
)

# Colocar entradas no submenu de ajuda
menu_ajuda.add_command(
    label='Ajuda',
    command=lambda: print(string_menu_ajuda.get())
)

# Criar um Checkbox no submenu de ajuda
string_menu_ajuda = tk.StringVar()
menu_ajuda.add_checkbutton(
    label='Check',
    onvalue='Ligado',
    offvalue='Desligado',
    variable=string_menu_ajuda
)

# Adicionar os submenus no menu principal
menu.add_cascade(
    label='Arquivo',
    menu=menu_arquivo
)
menu.add_cascade(
    label='Ajuda',
    menu=menu_ajuda
)

# Criar um botão no Menu
botao_menu = ttk.Menubutton(
    master=tela,
    text='Botão Menu'
)
botao_menu.pack()

# Criar um submenu dentro de "botao_menu"
botao_submenu = tk.Menu(
    master=botao_menu,
    tearoff=False
)
botao_submenu.add_command(
    label='Entrada 1',
    command=lambda: print('Teste 1')
)
botao_submenu.add_checkbutton(label='Check 1')
botao_menu['menu'] = botao_submenu

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
