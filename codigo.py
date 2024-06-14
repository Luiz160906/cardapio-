entradas = {
    'Ceviche de Salmão': 40.00,
    'Canudinho de Frango': 25.00,
    'Fondue': 42.00,
    'Caponata de berinjela': 35.00,
    'Pão de alho': 19.90
}

bebidas = {
    'Refrigerante': {
        'Coca-cola': 7.00,
        'Guaraná': 6.50,
        'Pepsi': 6.80,
        'Sprite': 6.50,
        'Guaravita': 5.50
    },
    'Sucos': {
        'Suco de Laranja': 8.00,
        'Suco de Abacaxi': 8.00,
        'Suco de Maracujá': 8.00,
        'Suco de Morango': 8.00,
        'Suco de Manga': 8.00
    },
    'Agua': {
        'Água sem gás': 5.00,
        'Água saborizada': 8.00,
        'Água com gás': 5.50
    },
    'Chas': {
        'Chá verde': 5.50,
        'Chá inglês': 7.00,
        'Chá de boldo': 6.00,
        'Chá de canela': 6.50,
        'Chá de camomila': 5.00
    }
}

pratop = {
    'Risoto de cogumelos com ancho': 40.00,
    'Salmao defumado': 43.00,
    'Abadejo a vilarejo': 32.90,
    'Tonkotsu missô lámen': 38.00,
    'Bife ancho ao aligot de aipim': 45.00,
    'Sorrentini de costela com burrata': 42.00
}

sobremesa = {
    'Pudim': 5.00,
    'Petit Gateau': 12.00,
    'Pave': 9.90,
    'Torta de limão': 6.90,
    'Rocambole': 6.50
}
cardapio = {"entradas": entradas, "bebidas": bebidas, "prato principal": pratop, "sobremesas": sobremesa}
def get_key(categoria, item):
    if categoria in cardapio:
        if item in cardapio[categoria]:
            return item, cardapio[categoria][item]
        else:
            return None, "Item não encontrado"
    else:
        return None, "Categoria não encontrada"

def deletar(categoria, item):
    if categoria in cardapio:
        if item in cardapio[categoria]:
            del cardapio[categoria][item]
            print("Item deletado com sucesso!")
        else:
            print("O item não existe nessa categoria.")
    else:
        print("A categoria não existe.")

def alterar(categoria, item_atual, item_novo):
    if categoria not in cardapio:
        print(f"A categoria '{categoria}' não existe no cardápio.")
    else:
        if categoria == "bebidas":
            subcategoria = input("Digite a subcategoria da bebida (Refrigerante, Sucos, Agua, Chas):").strip().title()
            if subcategoria not in bebidas or item_atual not in bebidas[subcategoria]:
                print(f"O item '{item_atual}' não existe na subcategoria '{subcategoria}' ou a subcategoria não existe.")
            else:
                cardapio[categoria][subcategoria][item_novo] = cardapio[categoria][subcategoria].pop(item_atual)
                print(f"Item '{item_atual}' alterado para '{item_novo}' com sucesso.")
        elif item_atual in cardapio[categoria]:
            cardapio[categoria][item_novo] = cardapio[categoria].pop(item_atual)
            print(f"Item '{item_atual}' alterado para '{item_novo}' com sucesso.")
        else:
            print(f"O item '{item_atual}' não existe na categoria '{categoria}'.")


def menup():
    while True:
        print('******* MENU *******')
        print('* 1 Adicionar itens *')
        print('* 2 Excluir Itens *')
        print('* 3 Alterar itens do cardápio*')
        print('* 4  Buscar itens *')
        print('* 5 listar todos os itens do cardápio *')
        print('* 6 encerrar programa *')
        print('****************')
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            print('******* MENU *******')
            print('* 1. Adicionar entradas *')
            print('* 2. Adicionar prato principal *')
            print('* 3. Adicionar sobremesas*')
            print('* 4. Adiconar bebidas *')
            print('****************')
            opcaoadd = int(input("Digite o numero da opção da categoria desejada: "))
            if opcaoadd == 1:
                quant = int(input("Quantas entradas você quer adicionar: "))
                for i in range(quant):
                  new = str(input("Digite o item que você deseja adicionar:"))
                  neww = float(input("Digite o valor do novo item: "))
                  entradas[new]= neww
            elif opcaoadd == 2:
                quant = int(input("Quantos pratos principais você quer adicionar: "))
                for i in range(quant):
                  newp = str(input("Digite o item que você deseja adicionar:"))
                  newwp = float(input("Digite o valor do novo item: "))
                  pratop[newp]= newwp
            elif opcaoadd == 3:
                quant = int(input("Quantas sobremesas você quer adicionar: "))
                for i in range(quant):
                  news = str(input("Digite o item que você deseja adicionar:"))
                  newws = float(input("Digite o valor do novo item: "))
                  sobremesa[news]= newws
            elif opcaoadd == 4:
                    quant = int(input("Quantas bebidas você quer adicionar: "))
                    for i in range(quant):
                        sub = str(input("Digite a subcategoria do item: "))
                        newb = str(input("Digite o item que você deseja adicionar:"))
                        newwb = float(input("Digite o valor do novo item: "))
                        if sub in bebidas:
                            bebidas[sub][newb] = newwb
                        else:
                            bebidas[sub] = {newb: newwb}
                            print(f"Subcategoria: {sub} criada ")
            print(f"O cardapio atualizado ficou assim: {cardapio}")
            

        if opcao !=1 or opcao !=2 or opcao !=3 or opcao !=4 or opcao !=5 or opcao !=6:
            print('digite uma opção já existente')

        if opcao == 2:
            categoria_ = input("Categoria: ")
            item_ = input("Item: ")
            deletar(categoria_, item_)
            print(cardapio)
            menup()




        elif opcao == 3:
            categoria_ = input("Digite a categoria do item que deseja alterar: ").strip().lower()
            item_atual = input("Digite o nome atual do item: ").strip().title()
            item_novo = input("Digite o novo nome do item: ").strip().title()
            alterar(categoria_, item_atual, item_novo)

        
        

        if opcao == 4: 
            categoria_ = input("Digite a categoria do item que deseja buscar: ").lower()
            item_ = input("Digite o nome do item que deseja buscar: ").lower()
            retorno = get_key(categoria_, item_)
            if retorno is not None:
                    resultado, valor = retorno
                    print(f"item: {resultado}, valor: {valor}")
            else:
                print(retorno)

        if opcao == 5:
            print('Cardapio atual = ', cardapio)
            

        elif opcao == 6:
            print("programa encerrado!")
            break


print("Olá, bem vindo ao sistema do Restaurante KYS!")
while True:
    iniciar = input(str("Digite S para começar: "))
    if iniciar.lower() == "s":
        menup()
        break
