#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite um número inteiro: '))

lista = []
soma = 0
for i in range(n1+1, n2): 
    lista.append(i)
    soma += i
    
print(f'a soma de todos os numero entre {n1} e {n2} é: {soma}')