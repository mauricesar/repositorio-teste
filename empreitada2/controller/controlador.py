from model.modelo import Modelo
from view.visao import Visao

class Controlador:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

        self.visao.definir_acao_botao(self.mostrar_texto)

    def mostrar_texto(self):
        texto = self.visao.obter_texto_entrada()
        self.modelo.definir_texto(texto)
        self.visao.exibir_texto(self.modelo.obter_texto())