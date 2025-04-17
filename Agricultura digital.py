# Aplicação para Agricultura Digital (Soja e Milho)
# Cálculo de área e manejo de insumos

culturas = []

def menu():
    print("\n===== MENU =====")
    print("1. Inserir dados de plantio")
    print("2. Exibir dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Calcular pulverização de insumos")
    print("6. Explicação dos cálculos")
    print("7. Sair")
    return input("Escolha uma opção: ")

def explicacao_calculos():
    print("\n=== Explicação dos Cálculos ===")
    print("📌 Cálculo da área de plantio:")
    print("   - A área é calculada como um retângulo: largura (m) x comprimento (m).")
    print("\n📌 Cálculo da quantidade de fertilizante:")
    print("   - A aplicação de fertilizante é feita considerando a dose por hectare.")
    print("   - Como 1 hectare = 10.000 m², a quantidade total aplicada é:")
    print("     (Área em m² / 10.000) x Dose de fertilizante (kg/hectare).")
    print("\n📌 Cálculo de pulverização de insumos:")
    print("   - O insumo (ex: herbicida) é aplicado por metro quadrado (mL/m²).")
    print("   - Multiplicamos a área das ruas pelo volume aplicado por metro quadrado.")
    print("=" * 40)

def inserir_dados():
    print("\n=== Inserção de Dados ===")
    cultura = input("Digite a cultura (Soja ou Milho): ").capitalize()
    if cultura not in ["Soja", "Milho"]:
        print("🚨 Cultura inválida! Escolha entre Soja ou Milho.")
        return
    largura = float(input("Digite a largura do campo (m): "))
    comprimento = float(input("Digite o comprimento do campo (m): "))
    area = largura * comprimento
    fertilizante = float(input("Quantidade de fertilizante (kg por hectare): "))
    total_fertilizante = (area / 10000) * fertilizante

    culturas.append({"Cultura": cultura, "Área": area, "Fertilizante": total_fertilizante})
    print("\n✅ Dados inseridos com sucesso!")
    print("=" * 40)

def exibir_dados():
    print("\n=== 📋 DADOS CADASTRADOS ===")
    if not culturas:
        print("🚨 Nenhuma cultura cadastrada.")
        return
    for i, c in enumerate(culturas):
        print(f"\n🔹 [ID: {i}]")
        print(f"🌱 Cultura: {c['Cultura']}")
        print(f"📏 Área: {c['Área']:.2f} m²")
        print(f"🌾 Fertilizante: {c['Fertilizante']:.2f} kg")
    print("=" * 40)

def atualizar_dados():
    exibir_dados()
    try:
        idx = int(input("Digite o ID da cultura a ser atualizada: "))
        if idx < 0 or idx >= len(culturas):
            print("🚨 ID inválido!")
            return
        print("\n=== Atualização de Dados ===")
        cultura = input("Nova cultura (Soja ou Milho): ").capitalize()
        if cultura not in ["Soja", "Milho"]:
            print("🚨 Cultura inválida!")
            return
        largura = float(input("Nova largura (m): "))
        comprimento = float(input("Novo comprimento (m): "))
        area = largura * comprimento
        fertilizante = float(input("Nova quantidade de fertilizante (kg por hectare): "))
        total_fertilizante = (area / 10000) * fertilizante

        culturas[idx] = {"Cultura": cultura, "Área": area, "Fertilizante": total_fertilizante}
        print("\n✅ Dados atualizados com sucesso!")
        print("=" * 40)
    except ValueError:
        print("🚨 Entrada inválida! Tente novamente.")

def deletar_dados():
    exibir_dados()
    try:
        idx = int(input("Digite o ID da cultura a ser deletada: "))
        if idx < 0 or idx >= len(culturas):
            print("🚨 ID inválido!")
            return
        culturas.pop(idx)
        print("\n✅ Dados removidos com sucesso!")
        print("=" * 40)
    except ValueError:
        print("🚨 Entrada inválida! Tente novamente.")

def calcular_pulverizacao():
    print("\n=== 🚜 CÁLCULO DE PULVERIZAÇÃO ===")

    if not culturas:
        print("🚨 Nenhuma cultura cadastrada. Insira primeiro os dados de plantio.")
        return

    print("\n📌 Escolha uma das opções abaixo:\n")
    for i, c in enumerate(culturas):
        print(f"🔹 [{i}] {c['Cultura']} - Área: {c['Área']:.2f} m²")

    try:
        idx = int(input("\nDigite o número da cultura desejada: "))
        if idx < 0 or idx >= len(culturas):
            print("🚨 ID inválido!")
            return

        cultura = culturas[idx]["Cultura"]
        area = culturas[idx]["Área"]

        insumo = input("Digite o tipo de insumo (ex: herbicida, fungicida, inseticida): ").capitalize()
        dosagem = float(input(f"Quantidade de {insumo} aplicada por metro quadrado (mL/m²): "))
        ruas = int(input("Quantas ruas a lavoura tem? "))
        largura_rua = float(input("Qual a largura de cada rua (m)? "))

        area_total_ruas = ruas * largura_rua * (area / (largura_rua * ruas))
        total_insumo = area_total_ruas * dosagem

        print("\n✅ Cálculo realizado com sucesso!")
        print(f"🌱 Cultura: {cultura}")
        print(f"💧 Insumo aplicado: {insumo}")
        print(f"📏 Área total das ruas: {area_total_ruas:.2f} m²")
        print(f"🔹 Quantidade total de {insumo} necessária: {total_insumo:.2f} mL")
        print("=" * 40)

    except ValueError:
        print("🚨 Entrada inválida! Tente novamente.")

while True:
    opcao = menu()
    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        exibir_dados()
    elif opcao == "3":
        atualizar_dados()
    elif opcao == "4":
        deletar_dados()
    elif opcao == "5":
        calcular_pulverizacao()
    elif opcao == "6":
        explicacao_calculos()
    elif opcao == "7":
        print("👋 Saindo do programa...")
        break
    else:
        print("🚨 Opção inválida! Escolha novamente.")
        import csv

        # Lista para armazenar os dados das culturas
        culturas = []

        def adicionar_cultura():
            cultura = input("Digite a cultura (Soja ou Milho): ")
            area = float(input("Digite a área plantada (m²): "))
            fertilizante = float(input("Digite a quantidade de fertilizante usada (L): "))

            # Adicionar aos dados armazenados
            culturas.append({"cultura": cultura, "area_plantio": area, "quantidade_fertilizante": fertilizante})

            # Salvar no CSV
            salvar_csv(print("Arquivo 'dados_culturas.csv' salvo com sucesso!"))

            print("Dados inseridos com sucesso!")

        def salvar_csv():
            """Salva os dados cadastrados no arquivo CSV"""
            with open("dados_culturas.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["cultura", "area_plantio", "quantidade_fertilizante"])
                writer.writeheader()
                writer.writerows(culturas)

        def exibir_dados():
            print("\n=== Dados das Culturas Cadastradas ===")
            for i, cultura in enumerate(culturas, start=1):
                print(f"{i}. Cultura: {cultura['cultura']}, Área: {cultura['area_plantio']}m², Fertilizante: {cultura['quantidade_fertilizante']}L")

        # Menu principal
        while True:
            print("\n1. Adicionar Cultura")
            print("2. Exibir Dados")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                adicionar_cultura()
            elif opcao == "2":
                exibir_dados()
            elif opcao == "3":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida, tente novamente.")
