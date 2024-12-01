# Exercicio
"""
Você deve escrever uma função que compara dois dicionários e retorna as chaves que são comuns entre eles. Siga as instruções abaixo:

1) Crie uma função chamada encontrar_chaves_comuns que recebe dois dicionários como parâmetros.
2) A função deve retornar uma lista com as chaves que estão presentes em ambos os dicionários.

Por exemplo, para os dicionários:

dicionario_1 = {'a': 1, 'b': 2, 'c': 3}
dicionario_2 = {'b': 4, 'c': 5, 'd': 6}

A função deve retornar: ['b', 'c']

Certifique-se de que a ordem das chaves na lista resultante não importa.

"""

def encontrar_chaves_comuns(dicionario1, dicionario2):
    chaves_comuns = set(dicionario1.keys()) & set(dicionario2.keys())
    return list(chaves_comuns)

def main():
    dicionario_1 = {"a": 1, "b": 2, "c": 3}
    dicionario_2 = {"b": 4, "c": 5, "d": 6}

    chaves_comuns = encontrar_chaves_comuns(dicionario_1, dicionario_2)
    print("Chaves comuns:", chaves_comuns)

if __name__ == "__main__":
    main()
