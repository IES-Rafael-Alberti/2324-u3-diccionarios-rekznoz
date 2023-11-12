from src.main10 import es_numero, verificar_dni

def test_es_numero():
    assert es_numero(4) == True
    assert es_numero(7) == True
    assert es_numero(99) == True
    assert es_numero(0) == False
    assert es_numero(-1) == False
    assert es_numero(-99) == False

def test_verificar_dni():
    assert verificar_dni("12345678Z") == True
    assert verificar_dni("12345678A") == False
    assert verificar_dni("12345678z") == False