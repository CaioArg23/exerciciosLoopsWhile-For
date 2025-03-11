#Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

n1 = int(input('digite a base da conta: '))
n2 = int(input('digite o expoente da conta: '))

resultado = 0
while resultado == 0:
    resultado = pow(n1, n2)

print(f'{n1} elevado a {n2} = {resultado}')


#ou utlizando laco for

n1 = int(input('digite a base da conta: '))
n2 = int(input('digite o expoente da conta: '))

for i in range (n1, n2):
    resultado = pow(i)

print (f'{n1} elevado a {n2} = {resultado}')