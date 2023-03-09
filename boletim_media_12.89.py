#Faça um programa que leia o nome e duas notas de vários alunos e guarde
#tudo em uma lista composta. No final mostre um boletim contendo a média de cada
#um e permita que o usuário possa mostrar as notas de cada aluno individualmente

ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input("Deseja inserir outro aluno? [S/N]: "))
    if resposta in "Nn":
        break

print("-="*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>14}')
print("-"*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>13.1f}')
while True:
    print('-'*35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc]} são {ficha[opc]}")
print("<<<< VOLTE SEMPRE >>>>")
