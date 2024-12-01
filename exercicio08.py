# Exercicio
"""
Uma faculdade deseja gerenciar a lista de alunos matriculados em seus cursos. O objetivo é criar um sistema que mantenha um registro dos alunos e seus respectivos cursos. Para isso, siga os passos abaixo:


1) Implemente uma função chamada 'adicionar_aluno' que receba o nome, idade e curso como parâmetros e adicione um novo dicionário à lista 'alunos'.

2) Implemente uma função chamada 'remover_aluno' que receba o nome do aluno como parâmetro e remova o dicionário correspondente da lista.

3) Implemente uma função chamada 'listar_alunos' que exiba todos os alunos da lista, mostrando nome, idade e curso.

4) Tente executar o código que utiliza essas funções para testar se funcionam corretamente.
"""

# Lista de alunos
alunos = [
    {"nome": "Ana", "idade": 20, "curso": "Engenharia"},
    {"nome": "Carlos", "idade": 22, "curso": "Matemática"},
    {"nome": "Maria", "idade": 19, "curso": "História"},
    {"nome": "Lucas", "idade": 21, "curso": "Física"},
    {"nome": "Juliana", "idade": 20, "curso": "Química"},
]

def adicionar_aluno(alunos, nome, idade, curso):
    novo_aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(novo_aluno)

def remover_aluno(alunos, nome):
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            break

def listar_alunos(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

def main():
    # Teste das funções
    print("Lista de Alunos Inicial:")
    listar_alunos(alunos)

    adicionar_aluno(alunos, "Ricardo", 23, "Engenharia de Software")
    print("\nApós adicionar Ricardo:")
    listar_alunos(alunos)

    remover_aluno(alunos, "Carlos")
    print("\nApós remover Carlos:")
    listar_alunos(alunos)

if __name__ == "__main__":
    main()
