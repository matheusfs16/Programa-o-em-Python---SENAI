import tkinter as tk

def soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ + n2_
    resultado.config(text=soma)

def sub():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ - n2_
    resultado.config(text=soma)

def mult():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ * n2_
    resultado.config(text=soma)

def div():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ / n2_
    resultado.config(text=soma)

# Janela principal
root = tk.Tk()
root.geometry('250x370')
root.columnconfigure(5, weight=2)
root.rowconfigure(0, weight=0)

# Frame para operadores
quadro = tk.Frame(root, width=15, height= 15)
quadro.grid(row=4, column= 1)



# Input e texto numero 1
n1_label = tk.Label(root,text="N1",font=('arial',12))
n1 = tk.Entry(root, font=('arial',12))
n1_label.grid(padx=5, pady=5 ,row=0, column= 0)
n1.grid(row=0, column= 1)


# Input e texto numero 2
n2_label = tk.Label(root,text="N2",font=('arial',12))
n2 = tk.Entry(root, font=('arial',12))
n2_label.grid(pady=5 ,row=2, column= 0)
n2.grid(row=2, column= 1)   

# Soma
btn = tk.Button(quadro, text='+',font=('arial',10), height=1, width=2,command=soma)
btn.grid(padx=3,pady=3, row=4, column= 0)

# Subtração
btn = tk.Button(quadro, text='-',font=('arial',10), height=1, width=2,command=sub)
btn.grid(row=4, column= 1)

# Multiplicação
btn = tk.Button(quadro, text='x',font=('arial',10), height=1, width=2,command=mult)
btn.grid(padx=3,pady=3, row=5, column= 0)

# Divisão
btn = tk.Button(quadro, text='/',font=('arial',10), height=1, width=2,command=div)
btn.grid(row=5, column= 1)

# Resultado
resultado = tk.Label(root, text="=",font=('arial',10))
resultado.grid(row=6, column= 0)
root.mainloop()