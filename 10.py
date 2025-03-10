#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite um número inteiro: '))

print(f'os números inteiros entre {n1} e {n2} sao: ')

for i in range(n1+1, n2): 
    print(i)
