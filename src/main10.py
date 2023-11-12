
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

def verificar_dni(dni):
    """
    Verifica la validez de un número de Documento Nacional de Identidad (DNI) español.

    Argumentos:
        dni (str): El número de DNI que se va a verificar.

    return:
        bool: True si el número de DNI es válido, False en caso contrario.
    """
    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if len(dni) != 9:
        return False

    if not dni[:8].isdigit():
        return False

    numero = int(dni[:8])
    letra_correcta = tabla_letras[numero % 23]

    if letra_correcta == dni[8]:
        return True
    else:
        return False

if __name__ == "__main__":
        
    clientes = {}
    programa = ""

    while programa != "6":
        programa = input("Interacciones \n1- Agregar Cliente \n2- Borrar Cliente \n3- Mostrar Cliente \n4- Mostrar Clientes \n5- Mostrar Clientes preferentes \n6- Terminar \n> ")
        if programa == "1":

            dni = ""
            while not verificar_dni(dni):
                dni = input("DNI - ")

            nombre = input("Nombre - ")
            direccion = input("Direccion - ")

            telefono = ""
            while not es_numero(telefono):
                telefono = input("Telefono - ")

            email = input("E-Mail - ")
            preferente = input("El Cliente tiene preferencia [Si/No] ").lower()

            if preferente == "si":
                preferente = True 
            else:
                preferente = False

            cliente = {"nombre":nombre, "direccion":direccion, "telefono":telefono, "email":email, "Preferente":preferente}
            clientes[dni] = cliente

        if programa == "2":
            dni = input("Introduce el DNI del Cliente a Borrar ")
            if dni in clientes:
                clientes.pop(dni)
            else:
                print("No existe el cliente con el DNI", dni)

        if programa == "3":

            dni = ""
            while not verificar_dni(dni):
                dni = input("Introduce el DNI del Cliente a Mostrar ")

            if dni in clientes:
                print("DNI -", dni)
                for clave, valor in clientes[dni].items():
                    if clave == "Preferente":
                        if valor:
                            valor = "Si"
                        else:
                            valor = "No"
                    print(clave + " -", valor)
            else:
                print("No existe el cliente con el DNI", dni)

        if programa == "4":
            print("> Lista completa de Clientes")
            for clave, valor in clientes.items():
                print("DNI -",clave,"| Nombre -",valor["nombre"],"| Direccion -",valor["direccion"],"| Telefono -",valor["telefono"])

        if programa == "5":
            print("> Lista de Clientes Preferentes")
            for clave, valor in clientes.items():
                if valor["Preferente"]:
                    print("DNI -",clave,"| Nombre -",valor["nombre"],"| Direccion -",valor["direccion"],"| Telefono -",valor["telefono"])