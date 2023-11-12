
def es_numero_flotante(entrada):
    """
    Comprueba si la entrada proporcionada es un número entero positivo.

    Argumentos:
        entrada (str): La entrada que se va a comprobar.

    return:
        bool: True si la entrada es un número entero positivo, False en caso contrario.
    """
    try:
        numero = float(entrada)
        if numero > 0:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":

    cesta_de_compra = {}
    respuesta = ""

    while respuesta.lower() != 'n':
        articulo = input("Ingrese el nombre del artículo ")
        
        precio = ""
        while not es_numero_flotante(precio):
            precio = input("Ingrese el precio del artículo ")
        
        cesta_de_compra[articulo] = float(precio)

        respuesta = input("¿ Quieres agregar más articulos ? (S/N) ")

    print("\nLista de la compra")
    total = 0

    for i, (articulo, precio) in enumerate(cesta_de_compra.items(), 1):
        print(f"Articulo {i} {articulo} - Precio {precio}")
        total += precio

    print(f"Total {total}")
