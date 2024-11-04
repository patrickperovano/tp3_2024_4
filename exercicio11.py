# Exercicio
"""
Você foi solicitado a criar um programa que simula uma tabela de classificação do Campeonato Brasileiro de Futebol. Neste programa, você deve realizar as seguintes tarefas:

1) Crie uma lista chamada 'times' com pelo menos 10 nomes de times do Campeonato Brasileiro.
2) Crie um dicionário chamado 'classificacao' onde as chaves são os nomes dos times e os valores são suas respectivas pontuações. Inicialmente, todas as pontuações devem ser zero.
3) Crie uma função chamada 'atualizar_pontuacao' que recebe o nome de um time e a quantidade de pontos a ser adicionada e atualiza a pontuação do time no dicionário.
4) Exiba a tabela de classificação, ordenando os times pela pontuação de forma decrescente.

# Considere como critério de desempate a ordem alfabética dos nomes dos times.

"""


def atualizar_pontuacao(classificacao, time, pontos):
    pass  # Implemente a lógica para atualizar a pontuação


def exibir_classificacao(classificacao):
    pass  # Implemente a lógica para exibir a tabela de classificação


def main():
    times = [
        "Flamengo",
        "Palmeiras",
        "São Paulo",
        "Santos",
        "Corinthians",
        "Grêmio",
        "Atlético Mineiro",
        "Internacional",
        "Vasco",
        "Fluminense",
    ]
    classificacao = {time: 0 for time in times}

    # Exemplo de atualização de pontuação
    atualizar_pontuacao(classificacao, "Flamengo", 3)
    atualizar_pontuacao(classificacao, "São Paulo", 1)
    atualizar_pontuacao(classificacao, "Palmeiras", 2)
    atualizar_pontuacao(classificacao, "Santos", 1)
    atualizar_pontuacao(classificacao, "Corinthians", 3)
    atualizar_pontuacao(classificacao, "Grêmio", 2)
    atualizar_pontuacao(classificacao, "Atlético Mineiro", 1)
    atualizar_pontuacao(classificacao, "Internacional", 3)
    atualizar_pontuacao(classificacao, "Vasco", 1)
    atualizar_pontuacao(classificacao, "Fluminense", 2)

    exibir_classificacao(classificacao)


if __name__ == "__main__":
    main()
