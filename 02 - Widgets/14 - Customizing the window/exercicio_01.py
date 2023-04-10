# Criar uma tela do app que inicia no meio do monitor

import tkinter as tk

# Tela
tela = tk.Tk()
tela.title('Exercício 1')

# Descobrir a largura e altura do monitor
largura_monitor = tela.winfo_screenwidth()
altura_monitor = tela.winfo_screenheight()

# Colocar a tela do app no meio do monitor
largura_app = 600
altura_app = 400
left = largura_monitor // 2 - largura_app // 2
top = altura_monitor // 2 - altura_app // 2
tela.geometry(f'{largura_app}x{altura_app}+{left}+{top}')

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
