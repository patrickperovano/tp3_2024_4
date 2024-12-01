# Exercicio
"""
Você deve testar o tempo que leva para verificar se uma chave está presente em um dicionário e se um elemento está presente em uma lista. 

Para isso, siga os passos abaixo:

1. Crie uma lista chamada `minha_lista` que contenha 1.000.000 de números inteiros variando de 0 a 999.999.
2. Crie um dicionário chamado `meu_dicionario` que contenha as mesmas chaves que a lista, i.e., os números de 0 a 999.999, cada um mapeando seu próprio valor (ex: 0: 0, 1: 1, ...).
3. Escolha um número aleatório entre 100.000 e 999.999 e armazene em `numero_aleatorio`.
4. Meça e imprima o tempo necessário para verificar se `numero_aleatorio` está em `minha_lista`.
5. Meça e imprima o tempo necessário para verificar se `numero_aleatorio` é uma chave do `meu_dicionario`.


Explique o que você observou. Qual estrutura de dados é mais eficiente para verificar a presença de um elemento? 

A saída esperada deve ser semelhante a esta:
Tempo para verificar se o número está na lista: X segundos
Tempo para verificar se o número está no dicionário: Y segundos
"""

import time
import random

def main():
    # Criar a lista e dicionário
    minha_lista = list(range(1000000))
    meu_dicionario = {i: i for i in range(1000000)}

    # Escolher um número aleatório
    numero_aleatorio = random.randint(100000, 999999)

    # Medir o tempo para verificar na lista
    inicio_lista = time.time()
    presente_na_lista = numero_aleatorio in minha_lista
    tempo_lista = time.time() - inicio_lista

    # Medir o tempo para verificar no dicionário
    inicio_dicionario = time.time()
    presente_no_dicionario = numero_aleatorio in meu_dicionario
    tempo_dicionario = time.time() - inicio_dicionario

    # Imprimir os resultados
    print(f"Tempo para verificar se o número está na lista: {tempo_lista:.6f} segundos")
    print(f"Tempo para verificar se o número está no dicionário: {tempo_dicionario:.6f} segundos")

if __name__ == "__main__":
    main()

"""
Explicação:

- Criação da Lista e Dicionário: Criei minha_lista com 1000000 de números inteiros de 0 a 999999 e meu_dicionario com os mesmos números como chaves e valores.
- Número Aleatório: Escolhi um número aleatório entre 100000 e 999999.
- Medição de Tempo: Utilizei time.time() para medir o tempo necessário para verificar a presença do número na lista e no dicionário.
- Resultados: Imprimi o tempo necessário para ambas as verificações.
"""