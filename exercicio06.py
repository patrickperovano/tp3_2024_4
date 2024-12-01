# Exercicio
"""
Você foi encarregado de criar um programa para gerenciar uma frota de carros. Seu trabalho é implementar as seguintes funcionalidades:

1) Crie um dicionário para armazenar informações sobre cada carro, onde a chave é o número da placa do carro e o valor é outro dicionário que contém informações como o modelo, o ano e a quantidade de quilômetros rodados.

2) Implemente uma função chamada adicionar_carro que permita adicionar um novo carro ao dicionário, com as informações fornecidas pelo usuário.

3) Implemente uma função chamada listar_carros que imprime todos os carros registrados na frota de forma organizada.

4) Implemente uma função chamada atualizar_quilometragem que permita atualizar a quantidade de quilômetros rodados de um carro, dado seu número de placa.

Utilize o menu interativo abaixo para testar suas funções:

1 - Adicionar carro
2 - Listar carros
3 - Atualizar quilometragem
4 - Sair

Ao final, o programa deve continuar pedindo opções ao usuário até que ele escolha sair.
"""


def adicionar_carro(frota, placa, modelo, ano, quilometragem):
    frota[placa] = {'modelo': modelo, 'ano': ano, 'quilometragem': quilometragem}

def listar_carros(frota):
    if not frota:
        print("Nenhum carro registrado na frota.")
    else:
        for placa, info in frota.items():
            print(f"Placa: {placa}, Modelo: {info['modelo']}, Ano: {info['ano']}, Quilometragem: {info['quilometragem']} km")

def atualizar_quilometragem(frota, placa, quilometragem):
    if placa in frota:
        frota[placa]['quilometragem'] = quilometragem
        print(f"Quilometragem do carro com placa {placa} atualizada para {quilometragem} km.")
    else:
        print(f"Carro com placa {placa} não encontrado na frota.")

def main():
    frota = {}

    while True:
        print("\nMenu:")
        print("1 - Adicionar carro")
        print("2 - Listar carros")
        print("3 - Atualizar quilometragem")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = input("Digite o ano do carro: ")
            quilometragem = int(input("Digite a quilometragem do carro: "))
            adicionar_carro(frota, placa, modelo, ano, quilometragem)

        elif opcao == "2":
            listar_carros(frota)

        elif opcao == "3":
            placa = input("Digite a placa do carro: ")
            quilometragem = int(input("Digite a nova quilometragem do carro: "))
            atualizar_quilometragem(frota, placa, quilometragem)

        elif opcao == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
