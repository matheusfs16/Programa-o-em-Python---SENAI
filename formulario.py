import tkinter as tk
from tkinter import messagebox


colunas = 100

def variaveis():
    nome_ = nome.get()
    idade_ = idade.get()
    mail_ = mail.get()
    cep_ = cep.get()
    cidade_ = cidade.get()
    endereco_ = endereco.get()
    celular_ = celular.get()
    curso_ = curso.get()
    print('----'*10)
    print('Nome:',nome_)
    print('Idade:',idade_)
    print('E-mail:',mail_)
    print('CEP:',cep_)
    print('Cidade:',cidade_)
    print('Endereço:',endereco_)
    print('Celular:',celular_)
    print('Cursos:',curso_)
    messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso')


root = tk.Tk()
root.geometry('1700x750')
for i in range(colunas):
    root.columnconfigure(i, minsize= 50)
root.configure(background='lightcyan2')
root.columnconfigure(6, pad=100)
root.columnconfigure(4, minsize=200)


form =tk.Label(root, text="Formulário", font= ('arial', 30),bg='lightcyan2')
form.grid(row=0, column= 6)

nome_lb = tk.Label(root,text="Nome", font=('arial',20),bg='lightcyan2').grid(row=2,column= 3)
nome = tk.Entry(root,font=('arial',12))
nome.grid(row=2,column= 4, sticky='WE')


idade_lb = tk.Label(root,text="Idade", font=('arial',20),bg='lightcyan2').grid(pady=5,row=3,column= 3)
idade = tk.Entry(root,font=('arial',12))
idade.grid(pady=5,row=3,column= 4,sticky='WE')


mail_lb = tk.Label(root,text="E-mail", font=('arial',20),bg='lightcyan2').grid(pady=5,row=4,column= 3)
mail = tk.Entry(root,font=('arial',12))
mail.grid(pady=5,row=4,column= 4, sticky='WE')


cep_lb = tk.Label(root,text="CEP", font=('arial',20),bg='lightcyan2').grid(pady=5,row=5,column= 3)
cep = tk.Entry(root,font=('arial',12))
cep.grid(pady=5,row=5,column= 4, sticky='WE')


curso_lb = tk.Label(root,text="Cursos", font=('arial',20),bg='lightcyan2').grid(pady=5,row=2,column= 5)
curso = tk.Entry(root,font=('arial',12))
curso.grid(pady=5,row=2,column= 6, sticky='WE')

celular_lb = tk.Label(root,text="Celular", font=('arial',20),bg='lightcyan2').grid(pady=5,row=3,column= 5)
celular = tk.Entry(root,font=('arial',12))
celular.grid(pady=5,row=3,column= 6, sticky='WE')


endereco_lb = tk.Label(root,text="Endereço", font=('arial',20),bg='lightcyan2').grid(pady=5,row=4,column= 5)
endereco = tk.Entry(root,font=('arial',12))
endereco.grid(pady=5,row=4,column= 6, sticky='WE')


cidade_lb = tk.Label(root,text="Cidade", font=('arial',20),bg='lightcyan2').grid(pady=5,row=5,column= 5)
cidade = tk.Entry(root,font=('arial',12))
cidade.grid(pady=5,row=5,column= 6, sticky='WE')


enviar = tk.Button(root,text='Enviar',font=('arial',20),bg='white',command=variaveis)
enviar.grid(row=6, column=5, sticky="WE",padx=2)


root.mainloop()