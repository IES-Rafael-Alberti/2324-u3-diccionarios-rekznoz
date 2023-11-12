from src.main5 import calcular_creditos

def test_calcular_creditos():
    asignaturas = {}
    assert calcular_creditos(asignaturas) == 0
    asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quqmica': 5}
    assert calcular_creditos(asignaturas) == 15