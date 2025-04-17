import os

os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    horarios = []
    while True:
        print("Local?")
        print("1 - Quadra São Vito (Meneghel)")
        print("2 - Areia São Vito (Meneghel)")
        print("3 - Quadra Nova Americana")
        opcao = input("Escolha (1 a 3): ")
        quadras = {
            '1': "Quadra Meneghel",
            '2': "Areia Meneghel",
            '3': "Quadra Nova Americana"
        }
        quadra = quadras.get(opcao)
        if not quadra:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Opção {opcao} inválida. Tente novamente.")
            continue

        opcao = None
        while True:
            print("\nEscolha horários:")
            for idx, hora in enumerate(["18:30", "19:30", "20:30"], 1):
                status = "SELECIONADO" if hora in horarios else ""
                print(f"{idx} - {hora} {status}")
            print("0 - Confirmar")
            opcao = input("Escolha: ")
            mapa = {'1': "18:30", '2': "19:30", '3': "20:30"}
            if opcao == '0':
                if len(horarios) != 0:
                    break
                print("\n\nEscolha ao menos uma opção de horário")
            elif opcao in mapa:
                if mapa[opcao] in horarios:
                    horarios.remove(mapa[opcao])
                else:
                    horarios.append(mapa[opcao])
            else:
                print(f"Opção {opcao} inválida.")

        opcao = None
        while True:
            print("\nInício da automação?")
            print("1 - Aguardar 07h59m")
            print("2 - Iniciar agora")
            opcao = input("Escolha: ")
            if opcao == '1':
                inicio = "07h59m"
                break
            elif opcao == '2':
                inicio = "agora"
                break
            else:
                print(f"Opção {opcao} inválida. Tente novamente.")
                continue
            

        while opcao != 's':
            print("\nResumo:")
            print(f"Local: {quadra}")
            print(f"Horários: {horarios}")
            print(f"Início: {inicio}")
            opcao = input("Confirmar? (s/n): ").lower()
            if opcao == 's':
                return quadra, horarios, inicio
            elif opcao == 'n':
                print("Reiniciando...")
                break
            else:
                print(f"Opção {opcao} inválida. Tente novamente.")