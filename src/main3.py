
def es_numero_flotante(entrada):
    """
    Comprueba si la entrada proporcionada es un número positivo.

    Argumentos:
        entrada (str): La entrada que se va a comprobar.

    return:
        bool: True si la entrada es un número positivo, False en caso contrario.
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

def calcular_precio(tabla, objeto, kilos):
    """
    Calcula el precio total de un objeto en función de su precio por kilo y la cantidad de kilos.

    Argumentos:
        tabla (dict): Un diccionario que relaciona objetos con su precio por kilo.
        objeto (str): El nombre del objeto para el cual se debe calcular el precio.
        kilos (float): La cantidad de kilos del objeto.

    Devuelve:
        float: El precio total del objeto basado en su precio por kilo y la cantidad de kilos.
    """
    precio = tabla[objeto]
    precio_total = precio * kilos
    return precio_total

if __name__ == "__main__":

    precios_frutas = {
        'platano': 1.35,
        'manzana': 0.80,
        'pera': 0.85,
        'naranja': 0.70
    }
    
    fruta = ""
    while not verificar_existencia(precios_frutas,fruta):
        fruta = input("Introduce una fruta ").lower()
    
    kilos = ""
    while not es_numero_flotante(kilos):
        kilos = input("Introduce el número de kilos ")

    precio = calcular_precio(precios_frutas, fruta, float(kilos) )
    
    print(f"El precio de {kilos} kilos de {fruta} es {precio:.2f} €")
