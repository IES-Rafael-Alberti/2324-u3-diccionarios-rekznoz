
def obtener_nombres_campos(directorio_texto):
    """
    Extrae los nombres de los campos de la primera línea de la cadena de entrada.

    Argumentos:
        directorio_texto (str): La cadena de entrada que contiene los nombres de los campos separados por punto y coma y las filas de datos separadas por saltos de línea.

    return:
        list: Una lista de nombres de campos extraídos de la primera línea de la cadena de entrada.
    """
    lineas = directorio_texto.split('\n')
    nombres_campos = lineas[0].split(';')
    return nombres_campos

def crear_diccionario_clientes(directorio_texto, nombres_campos):

    """
    Extrae los nombres de los campos de la primera línea de la cadena de entrada y los devuelve como una lista.

    Argumentos:
        directorio_texto (str): La cadena de entrada que contiene los nombres de los campos separados por puntos y comas y las filas de datos separadas por saltos de línea.

    return:
        list: Una lista de nombres de campos extraídos de la primera línea de la cadena de entrada.
    """
    
    lineas = directorio_texto.split('\n')
    directorio_clientes = {}

    for linea in lineas[1:]:
        datos_cliente = linea.split(';')
        nif_cliente = datos_cliente[0]
        info_cliente = {}
        for i in range(1, len(nombres_campos)):
            campo = nombres_campos[i]
            valor = datos_cliente[i]
            if campo == 'descuento':
                valor = float(valor)
            info_cliente[campo] = valor
        directorio_clientes[nif_cliente] = info_cliente

    return directorio_clientes

if __name__ == "__main__":
    
    texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    nombres_campos = obtener_nombres_campos(texto)
    directorio_clientes = crear_diccionario_clientes(texto, nombres_campos)

    print(directorio_clientes)