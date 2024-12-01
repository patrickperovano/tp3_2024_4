# Exercicio
"""
Você foi encarregado de criar um sistema para armazenar e gerenciar informações de alunos de uma turma. Para isso, você deve usar um dicionário para facilitar a organização dos dados. 

Siga as etapas abaixo:

1. Crie um dicionário chamado `turma` que armazenará o nome do aluno como chave e a sua nota como valor.
2. Adicione 5 alunos ao dicionário com suas respectivas notas.
3. Implemente uma função chamada `calcular_media` que recebe o dicionário `turma` e retorna a média das notas.
4. Implemente uma função chamada `aluno_aprovado` que recebe o dicionário `turma` e uma nota mínima (que deve ser 7). A função deve retornar uma lista com os nomes dos alunos que foram aprovados.

Por exemplo, para o dicionário:

turma = {
    "Alice": 8,
    "Bob": 5,
    "Carlos": 6,
    "Diana": 9,
    "Eugenio": 7
}

A saída esperada para a função calcular_media seria 7.0 e para a função aluno_aprovado seria ["Alice", "Diana", "Eugenio"].
"""


def calcular_media(turma):
    total_notas = sum(turma.values())
    quantidade_alunos = len(turma)
    media = total_notas / quantidade_alunos
    return media

def aluno_aprovado(turma, nota_minima=7):
    aprovados = [aluno for aluno, nota in turma.items() if nota >= nota_minima]
    return aprovados

def main():
    turma = {"Alice": 8, "Bob": 5, "Carlos": 6, "Diana": 9, "Eugenio": 7}

    media = calcular_media(turma)
    print(f"Média das notas: {media}")

    aprovados = aluno_aprovado(turma)
    print(f"Alunos aprovados: {aprovados}")

if __name__ == "__main__":
    main()
