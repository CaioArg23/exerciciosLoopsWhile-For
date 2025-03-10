#Faça um programa que leia 5 números e informe o maior número.

contador = 0
a = 1
lista = []
while contador < 5:
    n1 = float(input('digite um número: '))
    contador = contador + 1
    lista.append(n1)

lista.sort()
print(f'o maior número é: {lista[4]}')