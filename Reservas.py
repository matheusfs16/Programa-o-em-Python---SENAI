nome1 = input("Nome Cliente ")
idade1 = int(input("Idade Cliente "))
nome2 = input("Nome Cliente ")
idade2 = int(input("Idade Cliente "))
nome3 = input("Nome Cliente ")
idade3 = int(input("Idade Cliente "))

print('----'*10)
cadastro = {
    nome1:idade1,
    nome2:idade2,
    nome3:idade3
}

valores = {"Simples":100.00, "Duplo":150.00, "Luxo":250.00
}


print('''Temos 3 opções disponíveis:
    Simples: R$ 100,00 por dia.
    Duplo: R$ 150,00 por dia.
    Luxo: R$ 250,00 por dia.
      ''')



print("----"*10)

cadastro = {
    nome1:{},
    nome2:{},
    nome3:{},
}

if idade1 >= 18:
    escolha_1 = input(f"Qual opção {nome1} vai escolher? ")
    dias_1 = float(input(f"Quantos dias {nome1} irá permanecer? "))
    total_1 = valores[escolha_1] * dias_1
    cadastro[nome1][escolha_1] = total_1

else:
    print(f'{nome1} é menor de idade e não pode alugar sem responsável.')
    del cadastro[nome1]

if idade2 >= 18:
    escolha_2 = input(f"Qual opção {nome2} vai escolher? ")
    dias_2 = float(input(f"Quantos dias {nome2} irá permanecer? "))
    total_2 = valores[escolha_2] * dias_2
    cadastro[nome2][escolha_2] = total_2
else:
    print(f'{nome2} é menor de idade e não pode alugar sem responsável.')
    del cadastro[nome2]
if idade3 >= 18:
    escolha_3 = input(f"Qual opção {nome3} vai escolher? ")
    dias_3 = float(input(f"Quantos dias {nome3} irá permanecer? "))
    total_3 = valores[escolha_3] * dias_3
    cadastro[nome3][escolha_3] = total_3
else:
    print(f'{nome3} é menor de idade e não pode alugar sem responsável.')
    del cadastro[nome3]

print("")
print("-----------------CADASTRO---------------")
print("")
print(cadastro)
