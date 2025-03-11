#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

n1 = int(input('digite o primeiro número do conjunto: '))
n2 = int(input('digite o último número do conjunto: '))
numeros.append(n2)
print(f'o maior número é: {numeros}')

numeros.append(n1)
numeros.sort()
print(f'o menor número é {numeros[0]}')

somador = 0
for i in numeros:
    somador = somador + i

print(f'a soma de todos os números é: {somador}')