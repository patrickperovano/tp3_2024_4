# Exercicio
"""
Você foi designado para criar uma lista de quadrados de números. Para isso, siga os passos abaixo:

1. Escreva uma função chamada 'calcular_quadrados' que receba um número inteiro n e retorne uma lista com os quadrados de todos os números de 1 até n (inclusive).

2. Use list comprehesion para gerar essa lista de quadrados.

3. No final, a função deve retornar a lista resultante.

# Exemplo de uso:

Se n for 5, a saída deve ser:
[1, 4, 9, 16, 25]

"""


def calcular_quadrados(n):
    return None


def main():
    n = int(input("Digite um número inteiro: "))
    quadrados = calcular_quadrados(n)
    print("Lista de quadrados:", quadrados)


if __name__ == "__main__":
    main()
