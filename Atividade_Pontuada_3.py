import os
# Inicio dos vetores
avioes = [0] * 4
assentos = [0] * 4
reservas = []
# Inicio das Funções
def encontrar_aviao(numero):
    for i in range(4):
        if avioes[i] == numero:
            return i
    return -1

def registrar_avioes():
    for i in range(4):
        avioes[i] = int(input(f'Insira o número do avião {i+1}: '))

def registrar_assentos():
    for i in range(4):
        assentos[i] = int(input(f'Quantidade de assentos para o avião {avioes[i]}: '))

def reservar_passagem():
    if len(reservas) >= 20:
        print('Erro: Limite global de 20 reservas atingido!')
        return

    numero = int(input('Digite o número do avião para reserva: '))
    idx = encontrar_aviao(numero)
# idx(Index)
    if idx == -1:
        print('Este avião não existe!')
    elif assentos[idx] <= 0:
        print('Não há assentos disponíveis para este avião!')
    else:
        nome = input('Digite o nome do passageiro: ')
        reservas.append({
            'numero_aviao': numero,
            'nome_passageiro': nome
        })
        assentos[idx] -= 1
        print(f'Reserva para {nome} realizada com sucesso!')

def consultar_aviao():
    num_busca = int(input('Digite o número do avião para consultar: '))
    idx = encontrar_aviao(num_busca)

    if idx != -1:
        print(f'Avião {num_busca} possui {assentos[idx]} assentos disponíveis.')
    else:
        print('Avião não encontrado.')

def consultar_passageiro():
    buscar_passageiro = input('Digite o nome do passageiro: ')
    encontrado = False

    for r in reservas:
        if r['nome_passageiro'].lower() == buscar_passageiro.lower():
            print(f"Passageiro {r['nome_passageiro']} está no avião {r['numero_aviao']}")
            encontrado = True

    if not encontrado:
        print("Passageiro não encontrado.")
# Função do menu
def menu():
    print("\n--- SISTEMA DE RESERVAS AÉREAS ---")
    print("1. Registrar número do avião")
    print("2. Registrar quantidade assentos")
    print("3. Reservar passagem aérea")
    print("4. Consulta por avião")
    print("5. Consulta por passageiro")
    print("6. Encerrar sistema")
# Incio do Loop
while True:
    menu()
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        registrar_avioes()
    elif opcao == 2:
        registrar_assentos()
    elif opcao == 3:
        reservar_passagem()
    elif opcao == 4:
        consultar_aviao()
    elif opcao == 5:
        consultar_passageiro()
    elif opcao == 6:
        print('Encerrando sistema...')
        break
    else:
        print("Opção inválida!")
# Encerrando Progama
