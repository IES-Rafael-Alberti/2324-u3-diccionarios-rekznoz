
def es_numero(entrada):
    """
    Comprueba si la entrada proporcionada es un número positivo.

    Argumentos:
        entrada (str): La entrada que se va a comprobar.

    return:
        bool: True si la entrada es un número positivo, False en caso contrario.
    """
    try:
        numero = int(entrada)
        if numero > 0:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":

    nombre = input("Ingresa tu nombre ")

    edad = ""
    while not es_numero(edad):
        edad = input("Ingresa tu edad ")

    direccion = input("Ingresa tu direccion ")

    telefono = ""
    while not es_numero(telefono):
        telefono = input("Ingresa tu teléfono ")

    usuario = {
        'nombre': nombre,
        'edad': edad,
        'direccion': direccion,
        'telefono': telefono
    }

    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
