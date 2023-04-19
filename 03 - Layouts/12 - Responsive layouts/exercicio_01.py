# Utilizando o arquivo main.py como base, criar o layout quando a tela do App
# for maior do que 1200 pixels de largura

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """Classe responsável por criar e configurar o App."""
    def __init__(self, tamanho_inicial):
        super().__init__()
        self.title('Layout Responsivo')
        self.geometry(f'{tamanho_inicial[0]}x{tamanho_inicial[1]}')

        # Criar um frame para limpar a tela quando o layout mudar
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill='both')

        NotificarTamanho(self,
                         {
                             600: self.criar_layout_medio,
                             300: self.criar_layout_pequeno,
                             1200: self.criar_layout_grande
                         }
                         )

        # Mostrar a tela
        self.mainloop()

    def criar_layout_pequeno(self):
        """Função responsável por criar o layout pequeno."""
        # Limpar a tela quando mudar o layout
        self.frame.pack_forget()

        # Criar o frame do layout
        self.frame = ttk.Frame(self)

        # Widgets
        ttk.Label(
            master=self.frame,
            text='Label 1',
            background='red'
        ).pack(expand=True, fill='both', padx=10, pady=5)

        ttk.Label(
            master=self.frame,
            text='Label 2',
            background='green'
        ).pack(expand=True, fill='both', padx=10, pady=5)

        ttk.Label(
            master=self.frame,
            text='Label 3',
            background='blue'
        ).pack(expand=True, fill='both', padx=10, pady=5)

        ttk.Label(
            master=self.frame,
            text='Label 4',
            background='yellow'
        ).pack(expand=True, fill='both', padx=10, pady=5)

        self.frame.pack(expand=True, fill='both')

    def criar_layout_medio(self):
        """Função responsável por criar o layout médio."""
        # Limpar a tela quando mudar o layout
        self.frame.pack_forget()

        # Criar o frame do layout
        self.frame = ttk.Frame(self)

        # Configurar o layout grid()
        self.frame.columnconfigure(
            index=(0, 1),
            weight=1,
            uniform='a'
        )
        self.frame.rowconfigure(
            index=(0, 1),
            weight=1,
            uniform='a'
        )
        self.frame.pack(expand=True, fill='both')

        # Widgets
        ttk.Label(
            master=self.frame,
            text='Label 1',
            background='red'
        ).grid(column=0, row=0, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 2',
            background='green'
        ).grid(column=1, row=0, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 3',
            background='blue'
        ).grid(column=0, row=1, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 4',
            background='yellow'
        ).grid(column=1, row=1, sticky='news', padx=10, pady=10)

    def criar_layout_grande(self):
        """Função responsável por criar o layout grande"""
        # Limpar a tela quando mudar o layout
        self.frame.pack_forget()

        # Criar o frame do layout
        self.frame = ttk.Frame(self)

        # Configurar o layout grid()
        self.frame.columnconfigure(
            index=(0, 1, 2, 3),
            weight=1,
            uniform='a'
        )
        self.frame.rowconfigure(
            index=0,
            weight=1,
            uniform='a'
        )
        self.frame.pack(expand=True, fill='both')

        # Widgets
        ttk.Label(
            master=self.frame,
            text='Label 1',
            background='red'
        ).grid(column=0, row=0, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 2',
            background='green'
        ).grid(column=1, row=0, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 3',
            background='blue'
        ).grid(column=2, row=0, sticky='news', padx=10, pady=10)

        ttk.Label(
            master=self.frame,
            text='Label 4',
            background='yellow'
        ).grid(column=3, row=0, sticky='news', padx=10, pady=10)


class NotificarTamanho:
    """Classe responsável por notificar à classe App() que o tamanho da tela mudou."""
    def __init__(self, tela, dic_tamanho):
        self.tela = tela
        self.tamanho_minimo_atual = None
        self.dic_tamanho = {chave: valor for chave, valor in sorted(dic_tamanho.items())}

        # Obter as informações da tela do App para chamar a função
        self.tela.bind('<Configure>', self.verificar_tamanho)

        # Atualizar a tela do App a cada iteração
        self.tela.update()

        # Setar as dimensões mínimas da tela para evitar erro
        min_largura = list(self.dic_tamanho)[0]
        min_altura = self.tela.winfo_height()
        self.tela.minsize(min_largura, min_altura)

    def verificar_tamanho(self, evento):
        """Função responsável por verificar o tamanho da tela a cada iteração do App."""
        if evento.widget == self.tela:
            largura = evento.width
            tamanho_verificado = None

            # Ativar o layout pequeno
            for tamanho_minimo in self.dic_tamanho:
                delta = largura - tamanho_minimo
                if delta >= 0:
                    tamanho_verificado = tamanho_minimo

            if tamanho_verificado != self.tamanho_minimo_atual:
                self.tamanho_minimo_atual = tamanho_verificado
                self.dic_tamanho[self.tamanho_minimo_atual]()


if __name__ == '__main__':
    # Executar o app
    App((400, 300))
