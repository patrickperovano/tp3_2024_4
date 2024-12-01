# Exercicio
"""
A Cifra de César é uma técnica simples de criptografia onde cada letra do alfabeto é deslocada um número fixo de posições. 
Por exemplo, com um deslocamento de 3, 

'A' se tornaria 'D', 
'B' se tornaria 'E'
'C' se tornaria 'F'
'D' se tornaria 'G'
'E' se tornaria 'H'
'F' se tornaria 'I'
'G' se tornaria 'J'
'H' se tornaria 'K'
'I' se tornaria 'L'
'J' se tornaria 'M'
'K' se tornaria 'N'
'L' se tornaria 'O'
'M' se tornaria 'P'
'N' se tornaria 'Q'
'O' se tornaria 'R'
'P' se tornaria 'S'
'Q' se tornaria 'T'
'R' se tornaria 'U'
'S' se tornaria 'V'
'T' se tornaria 'W'
'U' se tornaria 'X'
'V' se tornaria 'Y'
'W' se tornaria 'Z'
'X' se tornaria 'A'
'Y' se tornaria 'B'
'Z' se tornaria 'C'


Porém, com uma técnica de análise de frequência, podemos tentar descobrir o deslocamento utilizado e, assim, decifrar a mensagem.

Neste exercício, você deve implementar uma função chamada quebrar_cifra_cesar que recebe uma mensagem criptografada e tenta quebrar a cifra utilizando a análise de frequência das letras na língua portuguesa. A função deve retornar o deslocamento encontrado e a mensagem decifrada.

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

def calcular_frequencia(mensagem):
    frequencias = {}
    for char in mensagem:
        if char.isalpha():
            if char in frequencias:
                frequencias[char] += 1
            else:
                frequencias[char] = 1
    return frequencias

def cifra_de_cesar(texto, deslocamento):
    texto_criptografado = []
    for char in texto:
        if char.isalpha():
            deslocamento_real = deslocamento % 26
            codigo_base = ord('A') if char.isupper() else ord('a')
            char_criptografado = chr((ord(char) - codigo_base + deslocamento_real) % 26 + codigo_base)
            texto_criptografado.append(char_criptografado)
        else:
            texto_criptografado.append(char)
    return ''.join(texto_criptografado)

def quebrar_cifra_cesar(mensagem_cifrada):
    frequencias = calcular_frequencia(mensagem_cifrada)
    letra_mais_comum = max(frequencias, key=frequencias.get)
    
    letras_frequentes = ['A', 'E', 'O', 'S', 'R', 'I', 'D', 'T', 'N']
    
    possiveis_mensagens = []
    
    for letra in letras_frequentes:
        deslocamento = (ord(letra_mais_comum.upper()) - ord(letra.upper())) % 26
        mensagem_decifrada = cifra_de_cesar(mensagem_cifrada, -deslocamento)
        possiveis_mensagens.append((deslocamento, mensagem_decifrada))
    
    return possiveis_mensagens[0]

def main():
    mensagem_cifrada = """r phx ilp hylghqwh hud dwdu dv gxdv srqwdv gd ylgd, h uhvwdxudu qd yhoklfh d 
dgrohvfhqfld. srlv, vhqkru, qdr frqvhjxl uhfrpsru r txh irl qhp r txh ixl. hp 
wxgr, vh r urvwr h ljxdo, d ilvlrqrpld h glihuhqwh. vh vr ph idowdvvhp rv rxwurv, 
yd; xp krphp frqvrod-vh pdlv rx phqrv gdv shvvrdv txh shugh; pdlv idowr hx 
phvpr, h hvwd odfxqd h wxgr. r txh dtxl hvwd h, pdo frpsdudqgr, vhphokdqwh d 
slqwxud txh vh srh qd eduded h qrv fdehorv, h txh dshqdv frqvhuyd r kdelwr 
hawhuqr, frpr vh glc qdv dxwrsvldv; r lqwhuqr qdr djxhqwd wlqwd. xpd fhuwlgdr txh 
ph ghvvh ylqwh dqrv gh lgdgh srghuld hqjdqdu rv hvwudqkrv, frpr wrgrv rv 
grfxphqwrv idovrv, pdv qdr d plp. rv dpljrv txh ph uhvwdp vdr gh gdwd 
uhfhqwh; wrgrv rv dqwljrv irudp hvwxgdu d jhrorjld grv fdpsrv-vdqwrv. txdqwr dv 
dpljdv, dojxpdv gdwdp gh txlqch dqrv, rxwudv gh phqrv, h txdvh wrgdv fuhhp qd 
prflgdgh. gxdv rx wuhv iduldp fuhu qhod drv rxwurv, pdv d olqjxd txh idodp reuljd 
pxlwd yhc d frqvxowdu rv glflrqdulrv, h wdo iuhtxhqfld h fdqvdwlyd."""
    
    deslocamento, mensagem_decifrada = quebrar_cifra_cesar(mensagem_cifrada)

    print(f"Deslocamento: {deslocamento}")
    print(f"Mensagem decifrada: '{mensagem_decifrada}'")

if __name__ == "__main__":
    main()