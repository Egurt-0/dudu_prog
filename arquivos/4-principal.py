from agenda import add_contact, delete_contacts, view_contacts

def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. view contacts")
        print("2. add contacts")
        print("3. delete contacts")
        print("4. Exit")
        option = int(input("Chose a option: "))
        if option == 1:
            view_contacts()
        elif option == 2:
            add_contact('name')
        elif option == 3:
            delete_contacts()
        elif option == 4:
            break
        else:
            print("Opcao invalida meu maninho, tenta dnv ai, please")



main()