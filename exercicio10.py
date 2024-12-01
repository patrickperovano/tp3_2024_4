# Exercicio
"""
Uma empresa de videogame está analisando o desempenho de seus jogos lançados no último ano. Para isso, você deve criar um sistema que permite armazenar e analisar informações sobre esses jogos. 

Sua tarefa é criar um dicionário para armazenar informações sobre cada jogo, onde as chaves serão os nomes dos jogos e os valores serão outro dicionário contendo as seguintes informações:

- 'preco': preço do jogo
- 'vendas': número de cópias vendidas
- 'ano_lancamento': ano em que o jogo foi lançado

Após criar os dados de exemplo, implemente as seguintes funcionalidades:

1. Crie uma função chamada adicionar_jogo que recebe o dicionário de jogos, o nome do jogo e suas informações e adiciona o novo jogo ao dicionário.

2. Crie uma função chamada calcular_faturamento que recebe o dicionário de jogos e retorna o faturamento total com base no preço e nas vendas de cada jogo.

3. Crie uma função chamada listar_jogos que imprime o nome de todos os jogos lançados no último ano.

# Exemplo de uso:

jogos = {
    "Jogo A": {"preco": 59.99, "vendas": 10000, "ano_lancamento": 2023},
    "Jogo B": {"preco": 49.99, "vendas": 5000, "ano_lancamento": 2022}
}

adicionar_jogo(jogos, "Jogo C", {"preco": 39.99, "vendas": 15000, "ano_lancamento": 2023})
print("Faturamento total:", calcular_faturamento(jogos))
listar_jogos(jogos)

# Saída esperada:
# Faturamento total: 1449700.00
# Jogos lançados no último ano: Jogo A, Jogo C
"""


def adicionar_jogo(jogos, nome, info):
    jogos[nome] = info

def calcular_faturamento(jogos):
    faturamento_total = 0
    for info in jogos.values():
        faturamento_total += info['preco'] * info['vendas']
    return faturamento_total

def listar_jogos(jogos):
    ano_atual = 2023
    jogos_ultimo_ano = [nome for nome, info in jogos.items() if info['ano_lancamento'] == ano_atual]
    print("Jogos lançados no último ano:", ", ".join(jogos_ultimo_ano))

def main():
    jogos = {
        "Jogo A": {"preco": 59.99, "vendas": 10000, "ano_lancamento": 2023},
        "Jogo B": {"preco": 49.99, "vendas": 5000, "ano_lancamento": 2022},
    }

    adicionar_jogo(jogos, "Jogo C", {"preco": 39.99, "vendas": 15000, "ano_lancamento": 2023})
    print("Faturamento total: R$", calcular_faturamento(jogos))
    listar_jogos(jogos)

if __name__ == "__main__":
    main()