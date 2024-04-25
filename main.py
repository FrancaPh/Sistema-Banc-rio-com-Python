menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Saldo insuficiente para efetuar o saque.")
        elif valor > limite:
            print("Valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Sessão encerrada.")
        break

    else:
        print("Opção inválida. Por favor, selecione novamente.")
