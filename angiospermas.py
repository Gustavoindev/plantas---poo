from plantas import Planta

class Angiosperma(Planta):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo  

    def caracteristicas(self):
        return f"{self._nome}: tem flores, tem frutos e é do tipo: {self.tipo}."