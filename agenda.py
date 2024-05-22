contatos = []

def cadastrar_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito" : False}
    contatos.append(contato)

def visualizar_lista():
    print("\nLista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "🌟" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{favorito}{indice}. {nome_contato} - {telefone} - {email}")

def editar_contato(indice_contato, novo_nome, novo_telefone, novo_email):
    indice = indice_contato - 1
    if indice >= 0 and indice >= len(contatos):
        print("Não existe contato com esse número")
        return
    contatos[indice]["nome"] = novo_nome
    contatos[indice]["telefone"] = novo_telefone
    contatos[indice]["email"] = novo_email
    print(f"Contato {indice_contato} atualizado para {novo_nome}")

def trocar_favorito(indice_contato):
    indice = indice_contato - 1
    contatos[indice]["favorito"] = False if contatos[indice]["favorito"] else True

def visualizar_favoritos():
    print("\nLista de favoritos")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favorito = "🌟"
            nome_contato = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{favorito}{indice}. {nome_contato} - {telefone} - {email}")

def excluir_contato(indice_contato):
    indice = indice_contato - 1
    del contatos[indice]

while True:
    print("\n Menu da Agenda:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Ver favoritos")
    print("6. Excluir contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número do contato: ")
        email = input("Digite o email do contato: ")
        cadastrar_contato(nome, telefone, email)
    elif escolha == "2":
        visualizar_lista()
    elif escolha == "3":
        visualizar_lista()
        indice_contato = int(input("Digite o número do contato que deseja atualizar: "))
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        editar_contato(indice_contato, novo_nome, novo_telefone ,novo_email)
    elif escolha == "4":
        visualizar_lista()
        indice_contato = int(input("Digite o número do contato que marcar/desmarcar como favorito: "))
        trocar_favorito(indice_contato)
    elif escolha == "5":
        visualizar_favoritos()
    elif escolha == "6":
        indice_contato = int(input("Digite o número do contato que deseja excluir: "))
        excluir_contato(indice_contato)
    elif escolha == "7":
        break

print("Programa finalizado")