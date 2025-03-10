#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

n1 = int(input('digite um número entre 1 e 10 para fazer o calculo da tabuada: '))

for i in range (0, 11):
    multiplicacao = n1 *i
    print(f'{n1} X {i} = {multiplicacao}')