
def calcular_creditos(asignaturas):
    """
    Calcula el número total de créditos para un conjunto dado de asignaturas.

    Argumentos:
        asignaturas (dict): Un diccionario en el que las claves son los nombres de las asignaturas y los valores son el número de créditos para cada asignatura.

    return:
        int: El número total de créditos de todas las asignaturas.
    """
    total = 0
    for i in asignaturas.values():
        total += i
    return total

if __name__ == "__main__":

    asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quqmica': 5}

    for Clave, Valor in asignaturas.items():
        print(f"Asignatura {Clave} tiene {Valor} puntos")

    total_creditos = calcular_creditos(asignaturas)
    print(f"El total de puntos del curso {total_creditos}")