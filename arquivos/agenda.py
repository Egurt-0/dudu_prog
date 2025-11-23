import os


def add_contact(name):
    name = input("informe o nome:\n ")
    adress = input("informe o enredeco:\n ")
    phone = input("informe o telefone:\n ")

    contact = f"Nome: {name}\n, Endereco: {adress}\n, Phone: {phone}\n"
    
    with open("dados/exemplo1.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists("dados/exemplo1.txt"):
        print("A lista de contatos esta vazia")
        return
    with open("dados/exemplo1.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Lista de contatos: ")
    print(contacts)

def delete_contacts():
    if not os.path.exists("dados/exemplo1.txt"):
        print("A lista de contatos esta vazia")
        return
    with open("dados/exemplo1.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("contatin excluido com sucesso pai, fique dboa!")



