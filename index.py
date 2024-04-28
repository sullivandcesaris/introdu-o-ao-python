contacts = []

def showContacts(contacts):
    print("\nLista de Contatos")

    if not contacts:
        print("Nenhum contato encontrado.")
        return

    for index, contact in enumerate(contacts, start=1):
        favorite = "⭐" if contact["favorite"] else " "
        complete_contact = contact["name"] + " / " + contact["phone"] + " / " + contact["email"]


        print(f"{index}. {favorite} {complete_contact}")
    
    return

def addContact(contacts, name, phone, email):

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    }

    contacts.append(contact)

    print(f"Contato {name} foi adicionado com sucesso")
    return

def editContact(contacts, index, name, phone, email):

    contacts[index]["name"] = name
    contacts[index]["phone"] = phone
    contacts[index]["email"] = email

    print(f"\nContato {index + 1} foi editado com sucesso")
    return

def favoriteContact(contacts, index):
    if contacts[index]["favorite"]:
        contacts[index]["favorite"] = False
        print(f"\nContato {contacts[index]['name']} removido da lista de favoritos")
    else:
        contacts[index]["favorite"] = True
        print(f"\nContato {contacts[index]['name']} adicionado à lista de favoritos")
    return

def showFavoriteContacts(contacts):
    print("\nLista de Contatos Favoritos:")

    favorite_contacts = [contact for contact in contacts if contact["favorite"]]
    
    if not favorite_contacts:
        print("Nenhum contato favorito encontrado.")
        return
    
    for index, contact in enumerate(favorite_contacts, start=1):
        favorite = "⭐"
        complete_contact = contact["name"] + " / " + contact["phone"] + " / " + contact["email"]
        print(f"{index}. [{favorite}] {complete_contact}")
    
    return

def deleteContact(contacts, index):
    
    deleted_contact = contacts.pop(index)
    print(f"\nContato {deleted_contact['name']} removido com sucesso.")

while True:
    print("\n Menu do Gerenciamento de Contatos")
    print("1. Ver lista de contatos")
    print("2. Adicionar um contato")
    print("3. Editar um contato")
    print("4. Marcar/Desmarcar contato da lista de favoritos")
    print("5. Ver lista de favoritos")
    print("6. Remover um contato")
    print("7. Sair")

    choice = input("Digite a sua escolha: ")

    if choice == "1":
        showContacts(contacts)

    elif choice == "2":
        name = input("Nome: ")
        phone = input("Phone: ")
        email = input("Email: ")
    
        addContact(contacts, name, phone, email)

    elif choice == "3":
        showContacts(contacts)
        index = input("\nDigite o número do contato que deseja atualizar: ")
        
        index = int(index) - 1

        contact = contacts[index]
        
        print("\nDados atuais do contato selecionado:")
        print("Nome:", contact["name"])
        print("Telefone:", contact["phone"])
        print("Email:", contact["email"])
        
        name = input("\nNovo nome: ")
        phone = input("Novo telefone: ")
        email = input("Novo email: ")
        
        editContact(contacts, index, name, phone, email)

    elif choice == "4":
        showContacts(contacts)
        favorite_contact = int(input("\nDigite o número do contato que deseja tornar favorito: "))
        favorite_contact = favorite_contact - 1

        favoriteContact(contacts, favorite_contact)

    elif choice == "5":
        showFavoriteContacts(contacts)
        
    elif choice == "6":
        showContacts(contacts)
        delete_contact = int(input("\nDigite o número do contato que deseja remover da sua lista: "))
        delete_contact = delete_contact - 1

        deleteContact(contacts, delete_contact)

    elif choice == "7":
        break

print("Sistema Finalizado")