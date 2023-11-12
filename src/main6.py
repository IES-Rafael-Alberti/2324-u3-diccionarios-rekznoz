
def es_numero(entrada):
    """
    Comprueba si la entrada proporcionada es un número entero positivo.

    Argumentos:
        entrada (str): La entrada que se va a comprobar.

    return:
        bool: True si la entrada es un número entero positivo, False en caso contrario.
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

    informacion = {}
    respuesta = ""

    while respuesta.lower() != 'n':

        nombre = input("Ingresa el nombre ")

        edad = ""
        while not es_numero(edad):
            edad = input("Ingresa la edad ")

        email = input("Ingresa el email ")

        telefono = ""
        while not es_numero(telefono):
            telefono = input("Ingresa el telefono ")

        informacion['nombre'] = nombre
        informacion['edad'] = edad
        informacion['email'] = email
        informacion['telefono'] = telefono

        print("Contenido")
        for clave, valor in informacion.items():
            print(f"{clave}: {valor}")

        respuesta = input("Quieres ingresar más informacion ? (S/N) ")