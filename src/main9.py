
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

def verificar_existencia(tabla, objeto):
    """
    Comprueba si un objeto existe en una tabla dada.

    Argumentos:
        tabla (list): La tabla en la que buscar el objeto.
        objeto (any): El objeto cuya existencia se va a comprobar en la tabla.

    Devuelve:
        bool: True si el objeto existe en la tabla, False en caso contrario.
    """
    if objeto in tabla:
        return True
    else:
        return False
    
if __name__ == "__main__":

    facturas = {}
    facturas_pagadas = {}
    opcion = ""

    while opcion != '3':

        print("\nOpciones:")
        print("1. Añadir una nueva factura")
        print("2. Pagar una factura existente")
        print("3. Terminar")
        
        opcion = input("Elija una opción (1/2/3) ")
        
        if opcion == '1':
            numero_factura = input("Ingresa el número de factura ")

            if not verificar_existencia(facturas, numero_factura):

                coste_factura = ""
                while not es_numero_flotante(coste_factura):
                    coste_factura = input("Ingresa el coste de la factura ")

                facturas[numero_factura] = float(coste_factura)
            else: 
                print("Esta Factura ya existe")

        elif opcion == '2':
            numero_factura = input("Ingresa el número de factura que desea pagar ")
            if verificar_existencia(facturas, numero_factura):
                coste_pagado = facturas.pop(numero_factura)
                facturas_pagadas[numero_factura] = coste_pagado
            else:
                print("La factura especificada no existe en el registro")

        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3")

    cantidad_cobrada = sum(facturas_pagadas.values())
    cantidad_pendiente = sum(facturas.values())

    print(f"\nCantidad cobrada hasta el momento {cantidad_cobrada}")
    print(f"Cantidad pendiente de cobro {cantidad_pendiente}")

    print("Programa terminado")
