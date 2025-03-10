perguntaNota = float(input('digite sua nota: '))

for numero in perguntaNota:
    if numero >10 or numero <0:
        perguntaNota = float(input('digite sua nota: '))

else:
    print (f'voce digitou a nota {perguntaNota}')