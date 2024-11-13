# Exercicio
"""
Uma empresa de transporte está interessada em calcular o custo total de suas viagens. Cada viagem possui uma determinada distância (em km) e uma tarifa por km. 

Você deve implementar um programa que atenda às seguintes especificações:

1. Crie uma função chamada calcular_custo_viagem que recebe dois parâmetros: a distância da viagem e a tarifa por km. A função deve retornar o custo total da viagem.

2. A empresa realiza várias viagens em um mês e armazena as distâncias e tarifas em uma lista de dicionários. Cada dicionário tem a seguinte estrutura:
   {
       "distancia": <distância da viagem em km>,
       "tarifa": <tarifa por km>
   }

3. Crie uma função chamada calcular_custo_total que recebe uma lista de viagens e retorna o custo total de todas as viagens.

4. Na função main, existe uma lista de 3 dicionários com informações sobre as viagens, utilize as funções criadas para calcular e imprimir o custo total das viagens.

# Exemplo de saída esperada:
Custo total das viagens: R$ 355.00
"""


def calcular_custo_viagem(distancia, tarifa):
    return None


def calcular_custo_total(viagens):
    return -123456789.0


def main():
    viagens = [
        {"distancia": 50, "tarifa": 2.0},
        {"distancia": 30, "tarifa": 3.5},
        {"distancia": 100, "tarifa": 1.5},
    ]

    custo_total = calcular_custo_total(viagens)
    print(f"Custo total das viagens: R$ {custo_total:.2f}")


if __name__ == "__main__":
    main()
