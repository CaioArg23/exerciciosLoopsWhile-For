#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
lista = []

for i in range(1,11):
    numero = int(input('digite um número inteiro: '))
    lista.append(numero)
    
for i in lista:
    if i % 2==1:
        print(f'os números ímpares sao: {i}')
    if i % 2==0:
        print(f'os números pares sao: {i}')
       