#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = str(input('digite o seu nome: '))
idade = int(input('digite a sua idade: '))
salario = float(input('digite o seu salário: '))
sexo = str(input('digite o seu sexo (f ou m): '))
estadoCivil = str(input('digite seu estado civil: '))
caracteres = len(nome)
masculino = 'm'
feminino = 'f'

while caracteres <=3:
    nome = str(input('digite o seu nome (tem que haver mais de 3 caracteres): '))

while idade <=0 or idade >150:
    idade = int(input('houve algo de errado, digite a sua idade novamente: '))

while salario <= 0:
    salario = float(input('houve algo de errado, digite o seu salário: '))

while sexo != masculino and sexo != feminino:
    sexo = str(input('houve algo de errado, digite o seu sexo (f ou m) novamente: '))

while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    estadoCivil = str(input('houve algo de errado digite seu estado civil novamente: '))

else:
    print(f'aqui estáo suas informacoes: Nome: {nome}, idade: {idade}, salario: {salario}, sexo: {sexo}, estado civil: {estadoCivil}')