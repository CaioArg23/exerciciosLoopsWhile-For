#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input('digite o nome de usuário: '))
senha = str(input('digite sua senha: '))

while senha == usuario:
    senha = str(input('digite sua senha (a senha deve ser diferente do nome de usuário): '))

else: 
    print(f'seu nome de usuário é: {usuario}, e senha: {senha}')