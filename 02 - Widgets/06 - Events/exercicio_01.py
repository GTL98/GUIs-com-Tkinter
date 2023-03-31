# Printar "Mousewheel" quando o usuário apertar "shift" e mexer na rodinha do mouse no campo de texto

import tkinter as tk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('600x500')

# Widget
texto = tk.Text(master=tela)
texto.pack()
texto.bind('<Shift-MouseWheel>', lambda evento: print('Mousewheel'))

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
