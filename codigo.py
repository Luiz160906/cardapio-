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
