# Exercicio
"""
A Cifra de César é uma técnica de criptografia simples em que cada letra de uma mensagem é substituída por outra letra que se encontra um número fixo de posições à frente no alfabeto. 
Por exemplo, se o deslocamento for 3, a letra 'A' se torna 'D', 'B' se torna 'E', etc. 
Quando se alcança o final do alfabeto, ele se reinicia (por exemplo, 'Z' se torna 'C' com um deslocamento de 3).

Sua tarefa é criar uma função chamada cifra_de_cesar que receba duas entradas: uma string (o texto a ser criptografado) e um número inteiro (o deslocamento). A função deve retornar a string criptografada usando a Cifra de César.

A função deve lidar apenas com letras do alfabeto inglês (de A a Z e de a a z) e ignorar quaisquer outros caracteres.

Abaixo está o esqueleto de código para que você possa implementar a função e testar seu funcionamento.
"""


def cifra_de_cesar(texto, deslocamento):
    return None


def main():
    # Testes
    texto = "hello, world!"
    deslocamento = 3
    resultado = cifra_de_cesar(texto, deslocamento)
    print(f"Texto original: {texto}")
    print(f"Texto criptografado: {resultado}")


if __name__ == "__main__":
    main()
