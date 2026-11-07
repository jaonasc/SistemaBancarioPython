saldo = 0.0
extrato = []
limite_saque = 500.0
limite_saques = 3
numero_de_saques = 0

print(f"Saldo inicial: R$ {saldo:.2f}")

while True:

    print("\n===== BANCO PYTHON =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Obrigado por utilizar o nosso sistema")
        break
    elif opcao == "2":
        valor = float(input("Qual o valor do deposito: R$ "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso")
        else:
            print("O valor de depósito deve ser positivo")
    elif opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "3":
        if numero_de_saques >= limite_saques:
            print("Limite de saque atingido!")
        else:
            valor = float(input("Valor do saque: R$ "))

            if valor <= 0:
                print("O valor do saque deve ser positivo!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite_saque:
                print("O limite por saque é de R$ 500,00")
            else:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_de_saques += 1
                print("Saque realizado com sucesso")
    elif opcao == "4":
        print("\n===== EXTRATO BANCARIO =====")
        if len(extrato) == 0:
            print("Nenhuma movimentação registrada!")
        else:
            for operacao in extrato:
                print(operacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Opção invalida, tente novamente!")