import csv

def gerar_projecao(orcamento, nome_arquivo="projecao_locacao.csv"):
    aluguel_mensal = orcamento.calcular_aluguel_mensal()
    valor_parcela = orcamento.calcular_parcela_contrato()
    quantidade_parcelas = orcamento.parcelas_contrato

    with open(
        nome_arquivo,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        escritor.writerow([
            "Mes",
            "Aluguel Mensal (R$)",
            "Taxa Contratual (R$)",
            "Total Previsto (R$)"
        ])

        for mes in range(1, 13):
            if mes <= quantidade_parcelas:
                taxa_mes = valor_parcela
            else:
                taxa_mes = 0.0

            total_mes = aluguel_mensal + taxa_mes

            escritor.writerow([
                mes,
                f"{aluguel_mensal:.2f}",
                f"{taxa_mes:.2f}",
                f"{total_mes:.2f}"
            ])

    print(f"\nProjeção gerada com sucesso: {nome_arquivo}")