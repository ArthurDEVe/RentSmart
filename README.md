# RentSmart — Sistema de Orçamento de Locação

- Funcionalidades:

* Cadastro das opções de locação por meio de perguntas no terminal;
* Cálculo do aluguel-base de apartamentos, casas e estúdios;
* Aplicação de adicionais de quartos e garagem;
* Cálculo das vagas de estacionamento para estúdios;
* Aplicação de desconto de 5% para apartamentos quando o cliente informa que não possui crianças;
* Cálculo e parcelamento da taxa contratual de R$ 2.000,00;
* Exibição de um resumo detalhado do orçamento;
* Geração de arquivo CSV com a projeção dos pagamentos durante 12 meses;
* Validação de entradas do usuário.

# Regras de negócio

| Tipo ou condição               | Regra                                             |
| ------------------------------ | ------------------------------------------------- |
| Apartamento de 1 quarto        | R$ 700,00 por mês                                 |
| Apartamento de 2 quartos       | R$ 900,00 por mês                                 |
| Casa de 1 quarto               | R$ 900,00 por mês                                 |
| Casa de 2 quartos              | R$ 1.150,00 por mês                               |
| Estúdio                        | R$ 1.200,00 por mês                               |
| Garagem em casa ou apartamento | Adicional de R$ 300,00 por mês                    |
| Pacote de 2 vagas para estúdio | R$ 250,00 por mês                                 |
| Vaga adicional em estúdio      | R$ 60,00 por mês                                  |
| Apartamento sem crianças       | Desconto de 5% sobre o aluguel após os adicionais |
| Taxa contratual                | R$ 2.000,00, parcelável em até 5 vezes            |

A taxa contratual é apresentada separadamente do aluguel mensal.

# Tecnologias utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Módulo `csv` da biblioteca padrão do Python

Não é necessária a instalação de bibliotecas externas para executar a versão atual do projeto.

# Estrutura do projeto

RentSmart/
├── main.py
├── imovel.py
├── orcamento.py
├── gerador_csv.py
└── README.md

* `main.py`: executa o programa e recebe as informações do usuário.
* `imovel.py`: contém a classe `Imovel` e o cálculo do aluguel-base.
* `orcamento.py`: contém a classe `Orcamento`, responsável pelos adicionais, descontos e condições contratuais.
* `projecao.py`: gera o arquivo CSV com a projeção de 12 meses.
* `teste_imovel.py`: arquivo de teste manual da classe `Imovel`.
* `README.md`: documentação do projeto.

# Como executar

Abra `main.py` e execute o código.

# Objetivos de aprendizagem

O projeto aplica conceitos de pensamento algorítmico e Programação Orientada a Objetos, incluindo:

* Classes e objetos.
* Atributos e métodos.
* Condicionais e estruturas de repetição.
* Funções para validação de entradas.
* Separação de responsabilidades.
* Manipulação de arquivos CSV.


Projeto acadêmico desenvolvido para a disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**. (Feito por Arthur Henrique)