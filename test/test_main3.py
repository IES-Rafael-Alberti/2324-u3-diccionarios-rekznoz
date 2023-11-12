from src.main3 import es_numero_flotante, verificar_existencia, calcular_precio
import pytest
def test_es_numero_flotante():
    assert es_numero_flotante(3.14) == True
    assert es_numero_flotante(0.5) == True
    assert es_numero_flotante(-3.14) == False
    assert es_numero_flotante(0) == False
    assert es_numero_flotante(1.0) == True
    assert es_numero_flotante(10.75) == True
    assert es_numero_flotante(-1.0) == False
    assert es_numero_flotante(-10.75) == False
    assert es_numero_flotante(100.99) == True
    assert es_numero_flotante(-100.99) == False

def test_verificar_existencia():
    tabla = [1, 2, 3, 4, 5]
    assert verificar_existencia(tabla, 3) == True
    assert verificar_existencia(tabla, 6) == False

def test_calcular_precio():
    precios_frutas = {
        'platano': 1.35,
        'manzana': 0.80,
        'pera': 0.85,
        'naranja': 0.70
    }
    objeto = 'manzana'
    kilos = 2
    assert calcular_precio(precios_frutas, objeto, kilos) == 1.6