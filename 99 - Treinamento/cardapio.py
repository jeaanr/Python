pedido = ""
carrinho = ""
burger = ""

menu = """
Bem vindo a Tupi burger

Esolha uma das opções:
1 - Cardápio
2 - Acompanhar pedido
3 - Reclamçaões e duvidas
4 - Cancelar solicitação

"""
cardapio = """

1 - Tupi Classico PCQ 
2 - Tupi Smash
3 - Tupi Bacon Burger 
4 - Tupi Veggie

"""

while True:
    operacao = input(menu)

    if operacao == 1:
        print({cardapio})
        if cardapio == 1:
            burger += "Tupi Classico"
            print(f"Produto adicionado ao carrinho" + "\nProdutos no carrinho: " + {carrinho})

            