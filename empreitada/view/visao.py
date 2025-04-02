import tkinter as tk
from tkinter import messagebox

class Visao:
    def __init__(self, root):
        self.root = root
        self.root.title("A primeira parte dos exercícios")
        self.root.geometry("400x300")

        self.rotulo_de_bem_vindo = tk.Label(root, text="Seja bem-vindo ao Tkinter", font=("Arial", 50))
        self.rotulo_de_bem_vindo.pack(pady=100)

        self.botao = tk.Button(root, text="Clique aqui imediatamente")
        self.botao.pack(pady=10)

    def definir_acao_botao(self, comando):
        self.botao.config(command=comando)

    def exibir_mensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)