
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
#mantidas as taxas de crescimento.

populacaoA = 8000
taxaCrescimentoA = 3/100

populacaoB = 200000
taxaCrescimentoB = 1.5/100
anos = 0    
while populacaoA < populacaoB:
    populacaoA += populacaoA * taxaCrescimentoA
    populacaoB += populacaoB * taxaCrescimentoB
    anos =  anos + 1

print(f'a populacao A vai levar {anos} anos para alcancar a populacao B')
    