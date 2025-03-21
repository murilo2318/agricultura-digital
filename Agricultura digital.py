def exibir_menu():
    print("\n--- Menu ---")
    print("1. Inserir dados da cultura")
    print("2. Calcular área plantada")
    print("3. Calcular manejo de insumos")
    print("4. Atualizar dados")
    print("5. Remover dados")
    print("6. Sair")
    
def inserir_dados():
    cultura = input("Digite a cultura (Soja ou Milho): ").capitalize()
    if cultura not in ["Soja", "Milho"]:
        print("Cultura inválida! Escolha Soja ou Milho.")
        return

    largura = float(input("Digite a largura da área plantada (m): "))
    comprimento = float(input("Digite o comprimento da área plantada (m): "))

    culturas.append({"cultura": cultura, "largura": largura, "comprimento": comprimento})
    print("Dados inseridos com sucesso!")

def calcular_area():
    for i, cultura in enumerate(culturas):
        area = cultura["largura"] * cultura["comprimento"]
        print(f"{i+1}. Cultura: {cultura['cultura']} | Área: {area} m²")

def calcular_insumos():
    taxa_fertilizante = float(input("Digite a quantidade de fertilizante por metro quadrado (litros/m²): "))
    
    for i, cultura in enumerate(culturas):
        area = cultura["largura"] * cultura["comprimento"]
        insumo_total = area * taxa_fertilizante
        print(f"{i+1}. Cultura: {cultura['cultura']} | Fertilizante necessário: {insumo_total:.2f} litros")

def atualizar_dados():
    calcular_area()
    indice = int(input("Digite o número da cultura para atualizar: ")) - 1
    if 0 <= indice < len(culturas):
        culturas[indice]["largura"] = float(input("Nova largura (m): "))
        culturas[indice]["comprimento"] = float(input("Novo comprimento (m): "))
        print("Dados atualizados com sucesso!")
    else:
        print("Índice inválido!")

def remover_dados():
    calcular_area()
    indice = int(input("Digite o número da cultura para remover: ")) - 1
    if 0 <= indice < len(culturas):
        del culturas[indice]
        print("Cultura removida com sucesso!")
    else:
        print("Índice inválido!")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        calcular_area()
    elif opcao == "3":
        calcular_insumos()
    elif opcao == "4":
        atualizar_dados()
    elif opcao == "5":
        remover_dados()
    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
