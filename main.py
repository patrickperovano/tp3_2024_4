from identificacao import nome, sobrenome

TP = "TP3"

if not nome or not sobrenome:
    print("Você deve adicionar seu nome e sobrenome na variável 'nome' e 'sobrenome'")
    raise Exception("Você deve adicionar seu nome e sobrenome na variável 'nome' e 'sobrenome'")

####################################################################
# Nao mexa nesse arquivo
# Para resolver o TP modifique os arquivos exercicio_*.py que podem ser acessados no lado esquerdo.
####################################################################

import os


def listar_exercicios():
    exercicios = [f for f in os.listdir("./") if f.endswith(".py") and "exercicio" in f]
    exercicios.sort()

    return exercicios


def escrever_cabecalho(i):
    WIDTH = 30
    print("")
    print(f"***** Exercício {i:02d} *****".center(WIDTH))


# Redireciona o stdout para o DualWriter
arquivos_exercicios = listar_exercicios()
arquivos_exercicios.sort()
for i in range(len(arquivos_exercicios)):
    escrever_cabecalho(i + 1)
    modulo = __import__(f"exercicio{i+1:02d}")
    if hasattr(modulo, "main"):
        modulo.main()
print("")
