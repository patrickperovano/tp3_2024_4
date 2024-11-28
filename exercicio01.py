# Exercicio
"""
Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor. Eles são bastante utilizados devido à sua flexibilidade e eficiência na busca de valores associados a uma chave específica. 
Sobre o funcionamento e as características dos dicionários em Python, responda às perguntas abaixo:
"""

# 1) O que é um dicionário em Python e qual a sua principal utilização?
"""
Dicionário é uma estrutura de dados em Python que armazena pares de chave-valor. 
Ele é utilizado na busca de valores associados a uma chave específica.
"""

# 2) Como você pode adicionar um novo par chave-valor a um dicionário existente? Dê um exemplo de código.
"""
dicionario = {'nome': 'Alice', 'idade': 25}
dicionario['cidade'] = 'São Paulo'
"""

# 3) Como você pode remover um item de um dicionário? Explique a diferença entre o método del e o método pop().
"""
del: Remove o par chave-valor de um dicionário.
pop(): Remove e retorna o valor associado à chave especificada.

del meu_dicionario['idade']
idade = meu_dicionario.pop('idade')
"""

# 4) Quais são algumas das principais operações que você pode realizar com dicionários, como acesso a valores, verificação de chaves, etc.?
"""
Acesso a valores: `meu_dicionario['chave']`
Verificação de chaves: `'chave' in meu_dicionario`
Iteração sobre chaves: `for chave in meu_dicionario`
Obter todas as chaves: `meu_dicionario.keys()`
Obter todos os valores: `meu_dicionario.values()`
Obter todos os itens (pares chave-valor): `meu_dicionario.items()`
"""