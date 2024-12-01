# Exercicio
"""
Você foi solicitado a criar um programa que simula uma tabela de classificação do Campeonato Brasileiro de Futebol. Neste programa, você deve realizar as seguintes tarefas:

1) Crie um dicionário chamado 'classificacao' onde as chaves são os nomes dos times e os valores são suas respectivas pontuações. Inicialmente, todas as pontuações devem ser zero.
2) Crie uma função chamada 'atualizar_pontuacao' que recebe o nome de um time e a quantidade de pontos a ser adicionada e atualiza a pontuação do time no dicionário.
3) Exiba a tabela de classificação, ordenando os times pela pontuação de forma decrescente.

# Considere como critério de desempate a ordem alfabética dos nomes dos times.

"""

def atualizar_pontuacao(classificacao, time, pontos):
    if time in classificacao:
        classificacao[time] += pontos
    else:
        classificacao[time] = pontos

def exibir_classificacao(classificacao):
    classificacao_ordenada = sorted(classificacao.items(), key=lambda x: (-x[1], x[0]))
    print("Tabela de Classificação:")
    for time, pontos in classificacao_ordenada:
        print(f"{time}: {pontos} pontos")

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
    # Inicialize um dicionário com 0 para todos os times
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
