#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fatorial = int(input('digite um número inteiro que vou calcular o fatorial do número: '))
resultado = 1

print(f'{fatorial}!=', end="")
for i in range(fatorial, 0, -1):  
    if i == 1:
        print(i, end="")  
    else:
        print(i, end=".")

for i in range(1, fatorial + 1):
    resultado *= i

print(f'={resultado}') 