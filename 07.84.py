#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre:
#1Quantas pessoas foram cadastradas
#2As pessoas mais pesadas
#3As pessovesas mais leves

temporaria = []
principal = []
maior = menor = 0

#loop infinito
while True:
    temporaria.append(str(input("Nome: ")))
    temporaria.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria [1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()

    resposta = str(input("Deseja continuar? [S/N]: "))
    if resposta in "Nn":
        break

print('-='*30)
print(f"Os dados foram: {principal}")
print(f"Ao todo, você cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi de {maior}Kg")
print(f"O menor peso foi de {menor}Kg")

