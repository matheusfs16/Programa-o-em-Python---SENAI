# Exercícios: 

# UTILIZE VARIÁVEIS!!!!!! 

# Utilize as 5 concatenações, teste todas 

# 1 Imprima uma mensagem de boas-vindas na tela.

print('Bom dia')



# 2 Declare uma variável booleana verdadeiro
# com o valor True e imprima seu tipo

x  =  True
print(type(x))

# 3 Imprima o resultado da multiplicação de dois 
# números decimais de sua escolha

n1  =  5.2
n2  =  5.8
print(n1 * n2)

# 4 Imprima o resultado da divisão (/)de dois números inteiros 
# de sua escolha.

n1  = 10
n2  = 2
print(n1 / n2)


# 5 Imprima o resultado da subtração de dois 
# números inteiros de sua escolha

n1  = 10
n2  = 2
print(n1 - n2)


# 6 Imprima o resultado da divisão (//)inteira de dois números inteiros 
# de sua escolha.

n1  = 10
n2  = 2
print(n1 // n2)


# 7 Imprima o resultado da multiplicação de 4 números 
# decimais de sua escolha
n1  = 106.5
n2  = 2.4
n3 = 5.
n4  = 5.2
print(n1 * n2 * n3 * n4 )


# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, 
# imprima o dobro desse número

var  =  10
print(var ** 2)

# 9 Crie um sistema de cadastro com as estruturas que vc já 
# conhece(Use apenas input, print e variavel)
#nome, email, idade, cidade, gradução, estado civil 

print("----"*15)
print("Seja Bem-Vindo(a)!")
print("Preencha os campos abaixo")
print("----"*15)
print(" ")
nome = input ("Digite seu nome: ")
email = input("Email: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
graduacao = input("Graduação: ") 
estado_cv = input("Estado civíl: ")

print("----"*15)
print(" ")
print(f"------CADASTRO {nome}------")
print("")
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")
print(f"Graduação: {graduacao}")
print(f"Estado Civíl: {estado_cv}")

