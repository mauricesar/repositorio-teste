from model.modelo import Modelo
from view.visao import Visao

class Controlador:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

        self.visao.definir_acao_botao(self.mostrar_mensagem)

    def mostrar_mensagem(self):
        mensagem = self.modelo.obter_mensagem()
        self.visao.exibir_mensagem(mensagem)