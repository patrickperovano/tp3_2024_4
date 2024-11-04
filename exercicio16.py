
# Exercicio
"""
A Cifra de César é uma técnica simples de criptografia onde cada letra do alfabeto é deslocada um número fixo de posições. Por exemplo, com um deslocamento de 3, 'A' se tornaria 'D', 'B' se tornaria 'E', e assim por diante. Porém, com uma técnica de análise de frequência, podemos tentar descobrir o deslocamento utilizado e, assim, decifrar a mensagem.

Neste exercício, você deve implementar uma função chamada quebrar_cifra_cesar que recebe uma mensagem criptografada e tenta quebrar a cifra utilizando a análise de frequência das letras na língua portuguesa (ou outra língua à sua escolha). A função deve retornar o deslocamento encontrado e a mensagem decifrada.

Dicas:
- As letras mais frequentes na língua portuguesa são, em ordem: 'A', 'E', 'O', 'S', 'R', 'I', 'D', 'T', 'N'.
- Você pode contar a frequência de cada letra na mensagem criptografada e, com base nisso, tentar encontrar o deslocamento correto.

A sua implementação deverá considerar somente letras e ignorar espaços e pontuações.

Exemplo de uso:
# mensagem_cifrada = "Khoor Zruog"
# quebrar_cifra_cesar(mensagem_cifrada)
# Desejamos que a saída seja:
# Deslocamento: 3
# Mensagem decifrada: "Hello World"
"""

def quebrar_cifra_cesar(mensagem_cifrada):
    return None, None


def main():
    mensagem_cifrada = "Khoor Zruog"
    deslocamento, mensagem_decifrada = quebrar_cifra_cesar(mensagem_cifrada)

    print(f"Deslocamento: {deslocamento}")
    print(f"Mensagem decifrada: '{mensagem_decifrada}'")


if __name__ == "__main__":
    main()


Resposta e critérios de avaliação:


# Exercicio
"""
A Cifra de César é uma técnica simples de criptografia onde cada letra do alfabeto é deslocada um número fixo de posições. Por exemplo, com um deslocamento de 3, 'A' se tornaria 'D', 'B' se tornaria 'E', e assim por diante. Porém, com uma técnica de análise de frequência, podemos tentar descobrir o deslocamento utilizado e, assim, decifrar a mensagem.

Neste exercício, você deve implementar uma função chamada quebrar_cifra_cesar que recebe uma mensagem criptografada e tenta quebrar a cifra utilizando a análise de frequência das letras na língua portuguesa (ou outra língua à sua escolha). A função deve retornar o deslocamento encontrado e a mensagem decifrada.

Dicas:
- As letras mais frequentes na língua portuguesa são, em ordem: 'A', 'E', 'O', 'S', 'R', 'I', 'D', 'T', 'N'.
- Você pode contar a frequência de cada letra na mensagem criptografada e, com base nisso, tentar encontrar o deslocamento correto.

A sua implementação deverá considerar somente letras e ignorar espaços e pontuações.

Exemplo de uso:
# mensagem_cifrada = "Khoor Zruog"
# quebrar_cifra_cesar(mensagem_cifrada)
# Desejamos que a saída seja:
# Deslocamento: 3
# Mensagem decifrada: "Hello World"
"""

def quebrar_cifra_cesar(mensagem_cifrada):
    from collections import Counter

    # Frequência esperada das letras na língua portuguesa
    frequencia_portuguesa = "aeosridtn"  # Primeiras letras mais frequentes
    mensagens = mensagem_cifrada.lower()
    
    # Contando frequências das letras na mensagem
    contagem = Counter(c for c in mensagens if c.isalpha())
    letras_frequentes = contagem.most_common()

    # Encontrar o deslocamento
    for i in range(26):
        tentativa = ""
        for c in mensagens:
            if c.isalpha():
                deslocado = chr((ord(c.lower()) - ord('a') - i) % 26 + ord('a'))
                tentativa += deslocado.upper() if c.isupper() else deslocado
            else:
                tentativa += c
        if letras_frequentes[0][0] == 'e':  # Comparando com a letra mais frequente
            return i, tentativa

    return 0, mensagens  # Caso não tenha encontrado o deslocamento

def main():
    mensagem_cifrada = "Khoor Zruog"
    deslocamento, mensagem_decifrada = quebrar_cifra_cesar(mensagem_cifrada)

    print(f"Deslocamento: {deslocamento}")
    print(f"Mensagem decifrada: '{mensagem_decifrada}'")

if __name__ == "__main__":
    main()


Critérios de avaliação:
1. A implementação deve contar corretamente a frequência das letras na mensagem cifrada.
2. O deslocamento deve ser encontrado comparando a letra mais frequente da cifra com a letra 'E', que é a mais comum em português.
3. A mensagem decifrada deve ser corretamente exibida com a preservação de maiúsculas e minúsculas.
4. O código deve ser executável e fornecer exemplos de entrada e saída.