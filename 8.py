#Faça um programa que leia 5 números e informe a soma e a média dos números.

contador = 0

lista = []

while contador < 5:
    n1 = float(input('digite um número: '))
    contador = contador + 1
    lista.append(n1)
    
soma = lista[0] + lista [1] + lista [2] + lista [3] + lista [4]
media = soma/5
print(f'a soma dos números é: {soma}')
print(f'a média dos números é: {media}')