import tkinter as tk
import orm
from tkinter import messagebox


def add_film():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.add_films(nome, ano, nota)
    messagebox.showinfo("Filme cadastrado com sucesso!!!")

def update_film():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.update_data(id, nome, ano, nota)
    messagebox.showinfo("Your film has been update successflly!!!")


def delete_film():
    id = entry_id.get()
    orm.delete_film(id)
    messagebox.showinfo("Your film has been update successflly!!!")


# interface grafica
root = tk.Tk()
root.title("Filmes")

# rotulos e campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=1, pady=5)


label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=28, pady=5)

button_add = tk.Button(root, text="Adicionar", command=add_film)
button_add.grid(row=4, column=0, columnspan=2, pady=5)
button_update = tk.Button(root, text="Update", command=update_film)
button_update.grid(row=5, column=0, columnspan=2, pady=5)
button_delete = tk.Button(root, text="Delete", command=delete_film)
button_delete.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()