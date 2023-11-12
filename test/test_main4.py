from src.main4 import obtener_nombre_mes

def test_obtener_nombre_mes():
    assert obtener_nombre_mes(1) == 'enero'
    assert obtener_nombre_mes(2) == 'febrero'
    assert obtener_nombre_mes(3) == 'marzo'
    assert obtener_nombre_mes(4) == 'abril'
    assert obtener_nombre_mes(5) == 'mayo'
    assert obtener_nombre_mes(6) == 'junio'
    assert obtener_nombre_mes(7) == 'julio'
    assert obtener_nombre_mes(8) == 'agosto'
    assert obtener_nombre_mes(9) == 'septiembre'
    assert obtener_nombre_mes(10) == 'octubre'
    assert obtener_nombre_mes(11) == 'noviembre'
    assert obtener_nombre_mes(12) == 'diciembre'