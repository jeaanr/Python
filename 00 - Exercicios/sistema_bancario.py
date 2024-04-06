menu = """
ESCOLHA UMA DAS OPERAÇÕES
1. Saque
2. Depósito
3. Extrato 
4. Finalizar

===>
"""

LIMITE_DIARIO = 3
LIMITE_SAQUE = 500
saldo = 1000
contagem_saque = 0
extrato = ""



while True:

    operacao = input(menu)
    
    if operacao == "1":
        contagem_saque += 1
        if contagem_saque > LIMITE_DIARIO:
            print ("\nERRO: Limite de 3 saques diários execedido, tente novamente amanhã!")
        else:
            valor_do_saque = int(input("\nInforme o valor do saque: "))  
            if valor_do_saque > LIMITE_SAQUE:
               print ("\nERRO: Limite máximo da transferência é de R$500,00")
            else:
                saldo -= valor_do_saque
                extrato += "-" + str(valor_do_saque) + " "
                print(f"\nSeu saldo atual é: {saldo}")

    elif operacao == "2":
        valor_do_deposito = int(input("\nInforme o valor do depósito: "))
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            extrato += "+" + str(valor_do_saque)
            print(f"\nSeu saldo atual é: {saldo}")
        else:
            print(f"\nERRO: Digite um valor válido")

    elif operacao == "3":
        print({extrato})

    elif operacao == "4":
        break

    else:
        print("\nOperação inválida, digite novamente o que deseja realizar")