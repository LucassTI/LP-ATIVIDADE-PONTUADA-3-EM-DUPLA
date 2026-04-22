import os

# Inicializando listas com 4 espaços
avioes = [0] * 4
assentos = [0] * 4
reservas = []

def encontrar_aviao(numero):
    for i in range(4):
        if avioes[i] == numero:
            return i
    return -1

while True:
    print("\n--- SISTEMA DE RESERVAS AÉREAS ---")
    print("1. Registrar número do avião")
    print("2. Registrar quantidade assentos")
    print("3. Reservar passagem aérea")
    print("4. Consulta por avião")
    print("5. Consulta por passageiro")
    print("6. Encerrar sistema")

    opcao = int(input("\nEscolha uma opção: "))

    # OPÇÃO 1: Registrar aviões
    if opcao == 1:
        for i in range(4):
            avioes[i] = int(input(f'Insira o número do avião {i+1}: '))
    
    # OPÇÃO 2: Registrar assentos
    elif opcao == 2:
        for i in range(4):
            assentos[i] = int(input(f'Quantidade de assentos para o avião {avioes[i]}: '))
    
    # OPÇÃO 3: Reservar passagem
    elif opcao == 3:
        if len(reservas) >= 20:
            print('Erro: Limite global de 20 reservas atingido!')
        else:
            numero = int(input('Digite o número do avião para reserva: '))
            idx = encontrar_aviao(numero)

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
                assentos[idx] -= 1  # IMPORTANTE: Subtrai o assento ocupado
                print(f'Reserva para {nome} realizada com sucesso!')

    # OPÇÃO 4: Consulta por avião
    elif opcao == 4:
        num_busca = int(input('Digite o número do avião para consultar: '))
        idx = encontrar_aviao(num_busca)
        if idx != -1:
            print(f'Avião {num_busca} possui {assentos[idx]} assentos disponíveis.')
        else:
            print('Avião não encontrado.')

    # OPÇÃO 5: Consulta por passageiro
    elif opcao == 5:
        nome_busca = input('Digite o nome do passageiro: ')
        encontrado = False
        for r in reservas:
            if r['nome_passageiro'].lower() == nome_busca.lower():
                print(f"Passageiro {r['nome_passageiro']} está no avião {r['numero_aviao']}")
                encontrado = True
        if not encontrado:
            print("Passageiro não encontrado.")

    # OPÇÃO 6: Sair
    elif opcao == 6:
        print('Encerrando sistema...')
        break