from src.main11 import obtener_nombres_campos

def test_obtener_nombres_campos():
    texto = "nombre;edad;ciudad\nRafa;25;San Fernando\nGustavo;30;Valparaiso"
    assert obtener_nombres_campos(texto) == ["nombre", "edad", "ciudad"]