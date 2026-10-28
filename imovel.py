# ----------- Cálculo de Imóveis

class Imovel:
    def __init__(self, tipo, quartos):
        self.tipo = tipo
        self.quartos = quartos

    def calcular_aluguel_base(self):
        if self.tipo == "apartamento":
            return 700 if self.quartos == 1 else 900

        elif self.tipo == "casa":
            return 900 if self.quartos == 1 else 1150

        elif self.tipo == "estudio":
            return 1200

        else:
            raise ValueError("Tipo de imóvel inválido.")