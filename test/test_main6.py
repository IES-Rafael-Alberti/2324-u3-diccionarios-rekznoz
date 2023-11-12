from src.main6 import es_numero

def test_positive_integer_input():
    assert es_numero(4) == True
    assert es_numero(7) == True
    assert es_numero(99) == True
    assert es_numero(0) == False
    assert es_numero(-1) == False
    assert es_numero(-99) == False