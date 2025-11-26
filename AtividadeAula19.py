import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn =  conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
              cpf  TEXT,
              nome TEXT,
              email TEXT

              )   
              ''')
    conn.commit()
    conn.close() 
   

def inserir_usuario():
    cpf_ = cpf.get()
    nome_= nome.get()
    email_ = email.get()

    if cpf_ and nome_ and email_:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios VALUES (?,?,?)',(cpf_,nome_,email_))

        conn.commit()
        conn.close()
        messagebox.showinfo('','DADOS INSERIDOS COM SUCESSO!')
    else:
        messagebox.showwarning('','INSIRA TODOS OS DADOS SOLICITADOS')

    con = conectar()
    c = con.cursor()
    con.commit()
    con.close()
    mostrar_usuario()

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
        
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    user = c.fetchall()

    for us in user:
        tree.insert('','end',values= (us[0],us[1],us[2]))
    conn.close()

def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit =tree.item(selecao)['values'][0]
        novo_cpf = cpf.get()
        novo_nome = nome.get()
        novo_email = email.get()

        if novo_cpf and novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET  nome =?, email =?, cpf =? WHERE cpf =?',(novo_nome,novo_email,novo_cpf,dado_edit))

            conn.commit()
            conn.close()
            mostrar_usuario()
            messagebox.showinfo('','DADOS ATUALIZADOS COM SUCESSO!')
        else:
            messagebox.showwarning('','TODOS DADOS PRECISAM ESTAR PREENCHIDOS')

        con = conectar()
        c = con.cursor()
        con.commit()
        con.close()



def delete_usuario():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE cpf = ?',(user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo("","DADO DELETADO COM SUCESSO")
        mostrar_usuario()
    else:
        messagebox.showerror("",'ERRO AO DELETAR O DADO')



# INTERFACE

root = tk.Tk()
root.geometry('800x630')
root.title('CRUD - FORM')
root.iconbitmap('icone.ico')


tk.Label(root, text="FORMULÁRIO:", font= ('arial', 15)).grid(column=0, row=0,padx=10)

# DADOS

fr0 =  tk.Frame(root)
fr0.grid()

cpf_lb = tk.Label(fr0, text="CPF:", font= ('arial', 15))
cpf_lb.grid(column=0, row=1,padx=10,pady=10)

nome_lb = tk.Label(fr0, text="Nome:", font= ('arial', 15))
nome_lb.grid(column=0, row=2,padx=10,pady=10)

email_lb = tk.Label(fr0, text="E-mail:", font= ('arial', 15))
email_lb.grid(column=0, row=3,padx=10,pady=10)


cpf = tk.Entry(fr0,font=('arial',15))
cpf.grid(column=1, row=1,padx=10,pady=10)

nome = tk.Entry(fr0,font=('arial',15))
nome.grid(column=1, row=2,padx=10,pady=10)

email = tk.Entry(fr0,font=('arial',15))
email.grid(column=1, row=3,padx=10,pady=10)

# BOTÕES E FRAME DELES

fr = tk.Frame(root)
fr.grid(padx=10, columnspan=2)


btn_salvar = tk.Button(fr,text='SALVAR',font=('arial',15), command=inserir_usuario)
btn_salvar.grid(row=5, column=0,padx=10,pady=10)

btn_att = tk.Button(fr,text='ATUALIZAR',font=('arial',15),command=atualizar)
btn_att.grid(row=5, column=2,padx=10,pady=10)

btn_delete = tk.Button(fr,text='DELETAR',font=('arial',15),command=delete_usuario)
btn_delete.grid(row=5, column=3,padx=10,pady=10)

# TREE VIEW

fr2 =  tk.Frame(root)
fr2.grid()

colunas = ('CPF', 'NOME', 'E-MAIL')
tree =  ttk.Treeview(fr2, columns=colunas, show='headings', height=40)
tree.grid(row=6, column=0,padx=10, sticky='nsew')


for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)


criar_tabela()
mostrar_usuario()

root.mainloop()