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
notas = {
    'alunos':[''],
    'notas':['']
}

for i in range(tentativas):
    login = input("Digite seu nome de usuário: ")
    senha_login = int(input("Digite sua senha: "))
    
    if login == user and senha_login == senha:
        qtd = int(input("Quantos alunos? "))
        for x in range(qtd):
            nome = input("Nome do aluno: ")
            n1 = int(input("Digite a primeira nota: "))
            n2 = int(input("Digite a segunda nota: "))
            n3 = int(input("Digite a terceira nota: "))
            media = (n1 + n2 + n3) /3
            notas["alunos"].append(nome)
            notas['notas'].append(media)
            if media >= 7:
                print("Aluno Aprovado")
                print(f"A média das notas de {nome} é de {media}")
            elif media < 7 and media >= 5:
                print("Aluno de Recuperação")
                print(f"A média das notas de {nome} é de {media}")
            else:
                print("Aluno Reprovado")
                print(f"A média das notas de {nome} é de {media}")
            
        acesso = input("Deseja ver todas as médias?s/n")
        
            
        if acesso == 's':
            print("----"*10)
            for i in range(len(notas['alunos'])):
                if i != 0:
                    print(notas["alunos"][i], notas["notas"][i])
                    print("----"*10)

        espec = input('Deseja ver uma média especifica?s/n')

        if espec == 's':
            print("----"*10)
            for i in range(len(notas['alunos'])):
                if i != 0:
                    print(i, '-', notas["alunos"][i])
                
            escolha = int(input('Escolha o aluno: '))  
            print(notas["alunos"][escolha], notas["notas"][escolha])          


        print("Até a próxima!")
        break
        
    else:
        tentativas -= 1
        if tentativas == 1:
           print("Ultima tentativa, sua conta será bloqueada no próximo erro")
        elif tentativas >= 1:
            print("Usuário ou senha incorretos, tente novamente")
            print(f"Tentativas restantes: {tentativas}")
        else:
            pass

if tentativas == 0:
    print("Conta bloqueada")
else:
    pass
