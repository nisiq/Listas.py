#Aprimore o exercicio 9 mostrando no final:
#A soma de todos os valores pares digitados;
#A soma de todos os valores da 3º coluna;
#O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz [linha][coluna] = int(input(f"Digite um valor para [{linha+1}, {coluna+1}]: "))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]

    print()
print('-='*30)
print(f"A soma dos valores pares é {somapar}")

for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f"A soma dos valores da terceira coluna é: {somacoluna}")

for coluna in range(0, 3):
    if coluna  == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f"O maior valor da segunda linha é {maior}.")
