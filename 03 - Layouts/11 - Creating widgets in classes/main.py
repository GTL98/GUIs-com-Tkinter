import tkinter as tk
from tkinter import ttk


def criar_segmento(master, label_texto, botao_texto):
    """Função responsável por criar os widgets."""
    frame = ttk.Frame(master=master)

    # Layout grid()
    frame.columnconfigure(
        index=(0, 1, 2),
        weight=1,
        uniform='a'
    )
    frame.rowconfigure(
        index=0,
        weight=1
    )

    # Widgets
    ttk.Label(
        master=frame,
        text=label_texto
    ).grid(column=0, row=0, sticky='news')

    ttk.Button(
        master=frame,
        text=botao_texto
    ).grid(column=1, row=0, sticky='news')

    return frame


class Segmento(ttk.Frame):
    """Classe responsável por criar os widgets."""
    def __init__(self, master, label_texto, botao_texto):
        super().__init__(master=master)

        # Layout grid()
        self.columnconfigure(
            index=(0, 1, 2),
            weight=1,
            uniform='a'
        )
        self.rowconfigure(
            index=0,
            weight=1
        )

        # Widgets
        ttk.Label(
            master=self,
            text=label_texto
        ).grid(column=0, row=0, sticky='news')

        ttk.Button(
            master=self,
            text=botao_texto
        ).grid(column=1, row=0, sticky='news')

        # Colocar os widgets na tela
        self.pack(expand=True, fill='both', padx=10, pady=10)


# Tela
tela = tk.Tk()
tela.title('Retornar Widgets')
tela.geometry('400x600')

# Criar os Widgets com uma função
criar_segmento(tela, 'Label', 'Botão').pack(expand=True, fill='both', padx=10, pady=10)
criar_segmento(tela, 'Teste', 'Click').pack(expand=True, fill='both', padx=10, pady=10)
criar_segmento(tela, 'Olá', 'Blup').pack(expand=True, fill='both', padx=10, pady=10)
criar_segmento(tela, 'Tchau', 'Yohoo').pack(expand=True, fill='both', padx=10, pady=10)
criar_segmento(tela, 'Última Label', 'Sair').pack(expand=True, fill='both', padx=10, pady=10)

# Criar os widgets com uma classe
Segmento(tela, 'Label', 'Botão')
Segmento(tela, 'Teste', 'Click')
Segmento(tela, 'Olá', 'Blup')
Segmento(tela, 'Tchau', 'Yohoo')
Segmento(tela, 'Última Label', 'Sair')

if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
