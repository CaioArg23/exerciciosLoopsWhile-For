#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

fatorial = int(input('digite um número inteiro que vou calcular o fatorial dele: '))
resultado = 1
while fatorial < 0 or fatorial > 16:
    fatorial = int(input('Número inválido! Digite um número entre 0 e 16: '))

print(f'{fatorial}!=', end="")
for i in range(fatorial, 0, -1):  
    if i == 1:
        print(i, end="")  
    else:
        print(i, end=".")

for i in range(1, fatorial + 1):
    resultado *= i

print(f'={resultado}')  