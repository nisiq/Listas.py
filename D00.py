#Criar uma matriz agrupando nome e idade dos usuários.

vet = []
nomes = []

for s in range(3):
    vet.append(input('Nome: '))
    vet.append(input('Idade: '))
    nomes.append(vet[:])
    vet.clear()

print(nomes)
