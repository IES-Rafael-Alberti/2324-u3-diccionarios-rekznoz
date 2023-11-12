
def verificar_diccionario(palabra, diccionario):
    """
    Comprueba si un objeto existe en una tabla dada.

    Argumentos:
        diccionario (list): La tabla en la que buscar el objeto.
        palabra (string): El string cuya existencia se va a comprobar en la tabla.

    return:
        bool: True si el objeto existe en la tabla, False en caso contrario.
    """
    if palabra in diccionario:
        return True
    else:
        return False

def agregar_palabras(palabra, diccionario):
    """
    Esta función toma como entrada una cadena de pares de palabras separados por comas y un diccionario. 
    Divide la cadena en pares de palabras individuales y verifica si cada palabra ya se encuentra en el diccionario. 
    Si una palabra no está en el diccionario, agrega la palabra y su traducción al diccionario.

    Argumentos:
        palabra (str): Una cadena de pares de palabras separados por comas. Cada par de palabras consiste en una palabra y su traducción, separadas por dos puntos.
        diccionario (dict): Un diccionario que contiene traducciones de palabras.

    return:
        Nada. La función modifica el diccionario diccionario in situ al agregar nuevas traducciones de palabras.
    """
    pares = palabra.split(',')

    for par in pares:
        if not verificar_diccionario(par, diccionario):
            palabra, traduccion = par.strip().split(':')
            diccionario[palabra] = traduccion

def traducir_frase(frase, diccionario):
    """
    Traduce pares de palabras en una cadena y los agrega a un diccionario de traducciones de palabras.

    Argumentos:
        palabra (str): Una cadena que contiene pares de palabras separados por comas.
        diccionario (dict): Un diccionario que contiene traducciones de palabras.

    return:
        Nada. La función modifica el diccionario diccionario en su lugar al agregar nuevas traducciones de palabras.
    """
    palabras = frase.split()
    frase_traducida = []

    for palabra in palabras:
        traduccion = diccionario.get(palabra, palabra) 
        frase_traducida.append(traduccion)

    return ' '.join(frase_traducida)

if __name__ == "__main__":

    diccionario_traduccion = {
        "perro": "dog",
        "gato": "cat",
        "casa": "house"
    }

    entrada = input("Ingrese las palabras en español e inglés (separadas por dos puntos y palabras separadas por comas): ")

    agregar_palabras(entrada, diccionario_traduccion)

    frase_espanol = input("Ingrese una frase en español: ")

    frase_traducida = traducir_frase(frase_espanol, diccionario_traduccion)
    print(f"Frase traducida al inglés: {frase_traducida}")
