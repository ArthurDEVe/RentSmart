# Importando Sistemas
from imovel import Imovel
from orcamento import Orcamento
from gerador_csv import gerar_projecao
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)


# Validar Respostas
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(Fore.CYAN + mensagem))

            if minimo <= valor <= maximo:
                return valor

            print(Fore.RED + f'Digite um número entre {minimo} e {maximo}.')

        except ValueError:
            print(Fore.RED + 'Entrada inválida! Digite um número inteiro.')


# Validar Respostas Booleanas
def ler_sim_nao(mensagem):
    while True:
        resposta = input(Fore.CYAN + mensagem + " (s/n): ").strip().lower()

        if resposta in ("s", "sim"):
            return True

        if resposta in ("n", "nao", "não"):
            return False

        print(Fore.RED + 'Resposta inválida! Digite s ou n.')


# --- Iniciar Sistema RentSmart
def executar_rentsmart():
    print(Fore.GREEN + '\n=====  BEM-VINDO AO RENTSMART  =====')
    print("Sistema de orçamento - R.M Imóveis\n")

    print(Fore.GREEN + 'Escolha o tipo de imóvel:')
    print(Fore.GREEN + '1 -' + Fore.WHITE + ' Apartamento')
    print(Fore.GREEN + '2 -' + Fore.WHITE + ' Casa')
    print(Fore.GREEN + '3 -' + Fore.WHITE + ' Estúdio')

    opcao = ler_inteiro("Opção: ", 1, 3)

    tipos = {
        1: "apartamento",
        2: "casa",
        3: "estudio"
    }

    tipo = tipos[opcao]

    if tipo == "estudio":
        quartos = 0
    else:
        quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)

    imovel = Imovel(tipo, quartos)

    possui_garagem = False
    possui_criancas = True
    vagas_estudio = 0

    if tipo in ("apartamento", "casa"):
        possui_garagem = ler_sim_nao(
            "Deseja adicionar uma vaga de garagem?"
        )

    elif tipo == "estudio":
        print(Fore.GREEN + "\nEstacionamento do estúdio:")
        print("0 - Sem vagas")
        print("2 a 10 - Quantidade total de vagas")

        vagas_estudio = ler_inteiro(
            "Quantidade de vagas: ", 0, 10
        )

        if vagas_estudio == 1:
            print(Fore.WHITE +
                "O pacote inicial custa R$ 250,00 "
                "e inclui duas vagas."
            )
            vagas_estudio = ler_inteiro(Fore.RED +
                "Digite 0 para não contratar ou 2 a 10: ", 0, 10
            )

            while vagas_estudio == 1:
                print("Escolha 0 ou uma quantidade entre 2 e 10.")
                vagas_estudio = ler_inteiro(
                    "Quantidade de vagas: ", 0, 10
                )

    if tipo == "apartamento":
        possui_criancas = ler_sim_nao(
            "O cliente possui crianças?"
        )

    parcelas = ler_inteiro(
        "\nEm quantas parcelas pagar a taxa contratual (1 a 5)? ",
        1,
        5
    )

    orcamento = Orcamento(
        imovel = imovel,
        possui_garagem = possui_garagem,
        possui_criancas = possui_criancas,
        vagas_estudio = vagas_estudio,
        parcelas_contrato = parcelas
    )

    orcamento.exibir_resumo()
    gerar_projecao(orcamento)

if __name__ == "__main__":
    executar_rentsmart()