from src.main1 import obtener_simbolo_divisa

def test_obtener_simbolo_divisa():
    diccionario = {'USD': '$', 'EUR': '€', 'JPY': '¥'}
    divisa = 'USD'
    assert obtener_simbolo_divisa(diccionario, divisa) == True
    divisa = 'GBP'
    assert obtener_simbolo_divisa(diccionario, divisa) == False