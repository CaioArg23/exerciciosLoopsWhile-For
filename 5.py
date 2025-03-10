#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
populacaoA = float(input('digite o numero de habitantes da populacao A: '))
taxaCrescimentoA = float (input('digite a taxa de crescimento da populacao A (em %): '))
CrescimentoA = taxaCrescimentoA/100

populacaoB = float(input('digite o numero de habitantes da populacao B: '))
taxaCrescimentoB = float (input('digite a taxa de crescimento da populacao B (em %): '))

CrescimentoB = taxaCrescimentoB/100
anos = 0
while populacaoA > populacaoB:
    populacaoA = float(input('a populacao A deve ser menor que a B, digite novamente: '))

while CrescimentoA < CrescimentoB:
    CrescimentoA = float(input('a taxa de crescimento da populacao B deve ser menor que a taxa de crescimento da populacao A digite novamente: '))

while populacaoA < populacaoB:
    populacaoA += populacaoA * CrescimentoA
    populacaoB += populacaoB * CrescimentoB
    anos =  anos + 1

print(f'a populacao A vai levar {anos} anos para alcancar a populacao B')