# Exercicio
"""
Um restaurante deseja manter um registro dos pratos do dia e seus preços. Você deve ajudar a implementar um sistema simples para gerenciar esse registro. Para isso, siga as instruções abaixo:

1. Crie um dicionário chamado 'cardapio' que contenha pelo menos 5 pratos e seus respectivos preços.
2. Escreva uma função chamada 'adicionar_prato' que receba o nome do prato e seu preço como parâmetros, e adicione esse prato ao dicionário 'cardapio'.
3. Escreva uma função chamada 'remover_prato' que receba o nome do prato como parâmetro e remova o prato do dicionário.
4. Escreva uma função chamada 'listar_pratos' que exiba todos os pratos do cardápio junto com seus preços.
5. Escreva uma função chamada 'atualizar_preco' que receba o nome do prato e um novo preço, e atualize o preço do prato no cardápio.

Teste seus métodos criando inicialmente o cardápio e realizando algumas operações.
"""

def adicionar_prato(cardapio, nome, preco):
    cardapio[nome] = preco

def remover_prato(cardapio, nome):
    if nome in cardapio:
        del cardapio[nome]

def listar_pratos(cardapio):
    for nome, preco in cardapio.items():
        print(f"{nome}: R$ {preco:.2f}")

def atualizar_preco(cardapio, nome, novo_preco):
    if nome in cardapio:
        cardapio[nome] = novo_preco

def main():
    cardapio = {"Lasanha": 25.00, "Pizza": 30.00, "Hamburguer": 22.00, "Salada": 15.00, "Sopa": 10.00}

    print("Cardápio inicial:")
    listar_pratos(cardapio)

    adicionar_prato(cardapio, "Frango Grelhado", 20.00)
    print("\nApós adicionar 'Frango Grelhado':")
    listar_pratos(cardapio)

    remover_prato(cardapio, "Sopa")
    print("\nApós remover 'Sopa':")
    listar_pratos(cardapio)

    atualizar_preco(cardapio, "Pizza", 35.00)
    print("\nApós atualizar o preço de 'Pizza':")
    listar_pratos(cardapio)

if __name__ == "__main__":
    main()
