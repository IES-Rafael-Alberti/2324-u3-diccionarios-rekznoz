from src.main8 import verificar_diccionario, agregar_palabras

def test_verificar_diccionario():
    diccionario_traduccion = {
        "perro": "dog",
        "gato": "cat",
        "casa": "house"
    }
    palabra = 'perro'
    assert verificar_diccionario(palabra, diccionario_traduccion) == True
    palabra = 'hola'
    assert verificar_diccionario(palabra, diccionario_traduccion) == False

def test_agregar_palabras():
    diccionario = {}
    agregar_palabras("perro:dog", diccionario)
    assert diccionario == {"perro": "dog"}