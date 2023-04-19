# Utilizando a classe Segmento() do arquivo main.py, criar:
    # Uma entrada e um botão;
    # Devem estar na terceira coluna;
    # A entrada deve estar em cima do botão;
    # O texto do botão deve ser adicionado por um parâmetro

import tkinter as tk
from tkinter import ttk


class Segmento(ttk.Frame):
    """Classe responsável por criar os widgets."""
    def __init__(self, master, label_texto, botao_texto, exercicio_texto):
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
        self.criar_caixa_exercicio(exercicio_texto).grid(column=2, row=0, sticky='news')

        # Colocar os widgets na tela
        self.pack(expand=True, fill='both', padx=10, pady=10)

    def criar_caixa_exercicio(self, botao_texto):
        """Função responsável por criar a entrada e o botão na última coluna do App."""
        frame = ttk.Frame(self)

        # Widgets
        ttk.Entry(master=frame).pack(expand=True, fill='both')

        ttk.Button(
            master=frame,
            text=botao_texto
        ).pack(expand=True, fill='both')

        return frame


# Tela
tela = tk.Tk()
tela.title('Exercício 1')
tela.geometry('400x600')

# Criar os widgets e colocá-los no App
Segmento(tela, 'Label', 'Botão', 'Exercício 1')
Segmento(tela, 'Teste', 'Click', 'Exercício 2')
Segmento(tela, 'Olá', 'Blup', 'Exercício 3')
Segmento(tela, 'Tchau', 'Yohoo', 'Exercício 4')
Segmento(tela, 'Última Label', 'Sair', 'Exercício 5')


if __name__ == '__main__':
    # Mostrar a tela
    tela.mainloop()
