# Criar um submenu com 2 opções, 1 separador e 1 Checkbutton

import tkinter as tk
from tkinter import ttk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')

# Menu principal
menu_principal = tk.Menu(master=tela)

# Submenu
submenu = tk.Menu(
    master=menu_principal,
    tearoff=False
)

# Adicionar as opções ao submenu
submenu.add_command(
    label='Opção 1',
    command=lambda: print('Essa é a Opção 1')
)
submenu.add_command(
    label='Opção 2',
    command=lambda: print('Essa é a Opção 2')
)

# Adicionar o separador
submenu.add_separator()

# Adicionar o Checkbutton ao submenu
string_submenu_check = tk.StringVar()
submenu.add_checkbutton(
    label='Verificação',
    onvalue='Verificado',
    offvalue='Não verificado',
    variable=string_submenu_check
)
submenu.add_command(
    label='Verificar',
    command=lambda: print(string_submenu_check.get())
)

# Colocar o submenu no menu principal
menu_principal.add_cascade(
    label='Submenu',
    menu=submenu
)

# Colocar o menu na tela
tela['menu'] = menu_principal

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
