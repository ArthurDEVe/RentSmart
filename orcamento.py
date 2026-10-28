class Orcamento:
    TAXA_CONTRATUAL = 2000.00

    def __init__(
        self,
        imovel,
        possui_garagem=False,
        possui_criancas=True,
        vagas_estudio=0,
        parcelas_contrato=1
    ):
        self.imovel = imovel
        self.possui_garagem = possui_garagem
        self.possui_criancas = possui_criancas
        self.vagas_estudio = vagas_estudio
        self.parcelas_contrato = parcelas_contrato

        self.validar_dados()

    def validar_dados(self):
        if self.imovel.tipo not in ("apartamento", "casa", "estudio"):
            raise ValueError("Tipo de imóvel inválido.")

        if self.imovel.tipo == "estudio":
            if self.vagas_estudio not in (0, 2) and self.vagas_estudio < 2:
                raise ValueError(
                    "O estúdio permite 0 vagas ou um pacote inicial de 2 vagas."
                )

        if not 1 <= self.parcelas_contrato <= 5:
            raise ValueError(
                "A taxa contratual pode ser parcelada de 1 a 5 vezes."
            )

    def calcular_adicionais(self):
        adicionais = 0.0

        if self.imovel.tipo in ("apartamento", "casa"):
            if self.possui_garagem:
                adicionais += 300.00

        elif self.imovel.tipo == "estudio":
            if self.vagas_estudio >= 2:
                adicionais += 250.00
                adicionais += (self.vagas_estudio - 2) * 60.00

        return adicionais

    def calcular_desconto(self, valor_aluguel):
        if (
            self.imovel.tipo == "apartamento"
            and not self.possui_criancas
        ):
            return valor_aluguel * 0.05

        return 0.0

    def calcular_aluguel_mensal(self):
        aluguel_base = self.imovel.calcular_aluguel_base()
        adicionais = self.calcular_adicionais()
        subtotal = aluguel_base + adicionais
        desconto = self.calcular_desconto(subtotal)

        return subtotal - desconto

    def calcular_parcela_contrato(self):
        return self.TAXA_CONTRATUAL / self.parcelas_contrato

    def exibir_resumo(self):
        aluguel_base = self.imovel.calcular_aluguel_base()
        adicionais = self.calcular_adicionais()
        subtotal = aluguel_base + adicionais
        desconto = self.calcular_desconto(subtotal)
        aluguel_final = subtotal - desconto
        parcela = self.calcular_parcela_contrato()

        print('\n===== RENTSMART - ORÇAMENTO =====')
        print(f"Imóvel: {self.imovel.tipo.title()}")
        print(f"Quartos: {self.imovel.quartos}")
        print(f"Aluguel-base: R$ {aluguel_base:.2f}")
        print(f"Adicionais: R$ {adicionais:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Aluguel mensal: R$ {aluguel_final:.2f}")
        print(f"Taxa contratual: R$ {self.TAXA_CONTRATUAL:.2f}")
        print(f"Parcelas do contrato: {self.parcelas_contrato}")
        print(f"Valor por parcela: R$ {parcela:.2f}")
        print("=================================")