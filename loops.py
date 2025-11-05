# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
# n = 0
# while n < 100:
#     n += 1
#     print(n)


# # 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.
# nomes = []
# while len(nomes) < 10:
#     nomes.append(input("Digite um nome: "))
#     print(nomes)

# Crie um sistema de notas alunos, com as seguintes operações: Utilize While ou for 
continuar = "s"
user = "matheusfs"
senha = 1234
tentativas = 3

while tentativas != 0:
    login = input("Digite seu nome de usuário: ")
    senha_login = int(input("Digite sua senha: "))
    
    if login == user and senha_login == senha:
        while continuar == "s":
            n1 = int(input("Digite a primeira nota: "))
            n2 = int(input("Digite a segunda nota: "))
            n3 = int(input("Digite a terceira nota: "))
            media = (n1 + n2 + n3) /3
            print(f"A média das notas é de {media}")
            continuar = input("Deseja continuar?s/n")
        print("Até a próxima!")
        break
    else:
        tentativas -= 1
        print("Usuário ou senha incorretos, tente novamente")
        print(f"Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Conta bloqueada")
else:
    pass
