# Exercicio
"""
Você foi solicitado a extrair informações de um dicionário que contém nomes de pessoas como chaves e suas idades como valores. Sua tarefa é criar uma lista de apenas os nomes das pessoas que têm 18 anos ou mais.

Siga os passos abaixo:

1. Crie um dicionário chamado pessoas com pelo menos 5 entradas, onde as chaves são nomes de pessoas e os valores são suas idades.
2. Use list comprehensions para criar uma lista chamada maiores_de_idade que contenha apenas os nomes das pessoas cuja idade é maior ou igual a 18.

O resultado final deve ser impresso, mostrando a lista de nomes das pessoas que são maiores de idade.
"""


def main():
    pessoas = {"Alice": 21, "Bob": 17, "Charlie": 19, "Diana": 16, "Eve": 22}

    # Use list comprehension para criar a lista maiores_de_idade
    maiores_de_idade = []

    print("Maiores de idade:", maiores_de_idade)


if __name__ == "__main__":
    main()
