import tkinter as tk

class Visao:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrada de Texto")
        self.root.geometry("900x1300")

        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=20)

        self.botao = tk.Button(root, text="Mostrar Texto")
        self.botao.pack(pady=10)

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack(pady=20)

    def definir_acao_botao(self, comando):
        self.botao.config(command=comando)

    def obter_texto_entrada(self):
        return self.entrada.get()
    
    def exibir_texto(self, texto):
        self.label_resultado.config(text=texto)