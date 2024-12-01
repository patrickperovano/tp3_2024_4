# Exercicio
"""
Você precisa criar uma função que conte a frequência de cada palavra em um texto de entrada. Para isso, siga os passos abaixo:

1. Escreva uma função chamada contar_frequencia que aceite uma string como entrada. A função deve retornar um dicionário onde as chaves são as palavras e os valores são as quantidades de vezes que cada palavra aparece na string.
2. A função deve ignorar a capitalização (ou seja, "Python" e "python" devem ser considerados a mesma palavra).
3. Considere palavras separadas por espaços e pontuações como delimitações (como vírgulas, pontos, etc.).

Após implementar a função, teste-a com a string abaixo:

texto = "Python é uma linguagem de programação. Python é amplamente utilizado para desenvolvimento web, automação e ciência de dados. Python é ótimo!"

O resultado esperado para a função contar_frequencia deve ser um dicionário com a contagem de cada palavra.
"""

import string

def contar_frequencia(texto):
    # Remover pontuações
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    # Converter para minúsculas
    texto = texto.lower()
    # Dividir o texto em palavras
    palavras = texto.split()
    # Contar a frequência de cada palavra
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

def main():
    texto = "Python é uma linguagem de programação. Python é amplamente utilizado para desenvolvimento web, automação e ciência de dados. Python é ótimo!"
    frequencias = contar_frequencia(texto)
    print(frequencias)

if __name__ == "__main__":
    main()

"""
Critérios de avaliação
- A função `contar_frequencia` deve lidar corretamente com a capitalização das palavras.
- A função deve remover as pontuações. Para isso remova utilizando o string.punctuation
- O dicionário de saída deve conter as palavras e suas respectivas contagens corretas.
"""
