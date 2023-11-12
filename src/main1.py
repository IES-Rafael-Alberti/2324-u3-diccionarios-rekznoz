
def obtener_simbolo_divisa(diccionario, divisa):
    """
    Comprueba si un símbolo de divisa dado existe en un diccionario.

    Argumentos:
    diccionario (dict): Un diccionario que contiene símbolos de divisa como claves.
    divisa (str): El símbolo de divisa que se va a comprobar.

    return:
        bool: True si la divisa está presente en el diccionario, False en caso contrario.
    """
    if divisa in diccionario:
        return True
    else:
        return False
    
if __name__ == "__main__":

    diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    divisa = input("Introduce una divisa ")
    simbolo = obtener_simbolo_divisa(diccionario_divisas, divisa)

    if simbolo:
        print(f"El símbolo de {divisa} es: {diccionario_divisas[divisa]}")
    else:
        print("Divisa no encontrada")
