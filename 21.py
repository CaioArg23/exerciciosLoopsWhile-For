#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def raiz_quadrada_loop(n):
    i = 0
    while i * i <= n:  
        i += 1
    return i - 1  

def eh_primo(n):
    if n < 2:
        return False   

    raiz = raiz_quadrada_loop(n)   

    for i in range(2, raiz + 1):   
        if n % i == 0:
            return False  

    return True  


numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")