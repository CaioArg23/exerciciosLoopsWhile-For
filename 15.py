#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.

a, b = 0, 1
while a <= 90:
    print(a)
    a, b = b, a + b
