def obtener_nombre_mes(numero_mes):
    """
    Devuelve el nombre correspondiente del mes en español para un número de mes dado.

    Argumentos:
        numero_mes (int): El número que representa el mes.

    return:
        str: El nombre del mes en español correspondiente al número de entrada. Si el número de entrada no es un mes válido, devuelve False.

    """
    meses = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }

    if numero_mes in meses:
        return meses[numero_mes]
    else:
        return False

def formatear_fecha(fecha):
    """
    Formatea una fecha en el formato "dd/mm/yyyy" a "dd de mes de yyyy"

    Argumentos:
        fecha (str): La fecha de entrada en formato "dd/mm/yyyy"

    Devuelve:
        str: La fecha de entrada formateada como "dd de mes de yyyy"
    """
    partes = fecha.split('/')
    if len(partes) == 3:
        dia, mes, anio = map(int, partes)
        nombre_mes = obtener_nombre_mes(mes)
        if nombre_mes:
            return f"{dia} de {nombre_mes} de {anio}"
    
    return False

if __name__ == "__main__":

    fecha = input("Escribe un fecha (dd/mm/aaaa) ")
    fecha_formateada = formatear_fecha(fecha)
    
    if fecha_formateada:
        print(f"La fecha formateada es: {fecha_formateada}")
    else:
        print("Fecha con formato incorrecto")