class Modelo:
    def __init__(self):
        self.texto = ""

    def definir_texto(self, texto):
        self.texto = texto

    def obter_texto(self):
        return self.texto