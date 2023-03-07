#Faça um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
#No final mostre a matriz na tela com a formatação correta.

#lista com 3 listas internas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0,3):
    for coluna in range(0, 3):
        matriz [linha][coluna] = int(input(f"Digite um valor para [{linha+1}, {coluna+1}]: "))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()
