#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numeros = []


n1 = int(input('digite o primeiro número do conjunto: '))
n2 = int(input('digite o último número do conjunto: '))

while n1 <0 and n2>100:
    n1 = int(input('digite o primeiro número do conjunto (maior que zero): '))
    n2 = int(input('digite o último número do conjunto (menor que 1000): '))


numeros.append(n2)
print(f'o maior número é: {numeros}')

numeros.append(n1)
numeros.sort()
print(f'o menor número é {numeros[0]}')

somador = 0
for i in numeros:
    somador = somador + i

print(f'a soma dos números é: {somador}')