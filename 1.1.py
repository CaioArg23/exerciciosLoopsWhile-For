#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

perguntaNota = float(input('digite sua nota: '))

while perguntaNota <0 or perguntaNota > 10:
    perguntaNota = float(input('digite sua nota: '))

else:
    print (f'voce digitou a nota {perguntaNota}')