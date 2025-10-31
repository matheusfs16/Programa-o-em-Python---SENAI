e_commerce = {
'livros':{


'ARARI':50.0,
'TALEB':70.0,  


},
'tablets':{
    'SAMSUMG':15000.55,
    'NOKIA':456.5,
},
'fones':{
   'JBL':500.0,
   'APPLE':750.0, 
}


}



 
minhas_compras = {
'carrinho' : [],
'valores':[]
}



secao1 = input('livros, tablets ou fones ')
prod1 = input(f'{e_commerce[secao1]}')

minhas_compras['carrinho'].append(prod1)
minhas_compras['valores'].append(e_commerce[secao1][prod1])
print(minhas_compras)


secao2 = input('livros, tablets ou fones ')
prod2 = input(f'{e_commerce[secao2]}')

minhas_compras['carrinho'].append(prod2)
minhas_compras['valores'].append(e_commerce[secao2][prod2])
print(minhas_compras)


secao3 = input('livros, tablets ou fones ')
prod3 = input(f'{e_commerce[secao3]}')

minhas_compras['carrinho'].append(prod3)
minhas_compras['valores'].append(e_commerce[secao3][prod3])
print(minhas_compras)


soma =  sum(minhas_compras['valores'])
print(soma)



