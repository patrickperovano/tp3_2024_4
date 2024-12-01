# Exercicio
"""
Um dicionário é uma estrutura de dados em Python que armazena pares de chave-valor, enquanto uma lista é uma coleção ordenada de elementos. Sobre as principais diferenças entre dicionários e listas, responda às perguntas abaixo:
"""

# 1) Quais são as principais diferenças entre listas e dicionários em Python?
"""
Dicionários armazenam dados em pares de chave-valor
Listas armazenam dados em uma coleção ordenada de elementos.
"""

# 2) Quando você deve usar uma lista em vez de um dicionário e vice-versa?
"""
Listas: Quando a ordem importa
Dicionários: Quando precisa de uma busca rápida por chaves únicas.
"""

# 3) Como você pode iterar sobre os elementos de um dicionário em Python?
"""
Chaves: .keys()
Valores: .values()
Chave-valor: .items().
"""

# 4) Dê um exemplo de como você pode adicionar e remover elementos de um dicionário.
"""
Adicionar:

meu_dicionario = {}
meu_dicionario['nome'] = 'Alice'
print(meu_dicionario)  # Saída: {'nome': 'Alice'}

Remover usando del:
meu_dicionario = {'nome': 'Alice'}
del meu_dicionario['nome']
print(meu_dicionario)  # Saída: {}

Remover usando pop():
meu_dicionario = {'nome': 'Alice'}
nome = meu_dicionario.pop('nome')
print(meu_dicionario)  # Saída: {}
print(nome)  # Saída: Alice
"""
