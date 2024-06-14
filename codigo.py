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
