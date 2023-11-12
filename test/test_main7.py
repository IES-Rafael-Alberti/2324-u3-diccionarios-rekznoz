from src.main7 import es_numero_flotante

def test_es_numero_flotante():
    assert es_numero_flotante(3.14) == True
    assert es_numero_flotante(-2.5) == False