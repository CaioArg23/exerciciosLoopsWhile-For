#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

lista = []

for i in range(1, 51, 2):  # Começa em 1, vai até 50, pulando de 2 em 2 (apenas ímpares)
    lista.append(i)

print(lista)

#ou...

lista2 = []
for i in range(0, 51):
    if i % 2 ==1:
        lista2.append(i)
    
print (lista2)