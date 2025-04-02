import tkinter as tk
from model.modelo import Modelo
from view.visao import Visao
from controller.controlador import Controlador

def main():
    root = tk.Tk()

    modelo = Modelo()
    visao = Visao(root)
    controlador = Controlador(modelo, visao)

    root.mainloop()

if __name__ == "__main__":
    main()