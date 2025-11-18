import pytest
from main_pruebas import ejecutar_pruebas_login, ejecutar_pruebas_reservas


def test_login_basico():
    """Verifica que al menos un escenario de login funcione correctamente"""
    resultados = ejecutar_pruebas_login()
    exitosos = [r for r in resultados if r[1] == "OK"]
    assert len(exitosos) > 0, "Ningún escenario de login tuvo éxito"


def test_reservas_funcionan():
    """Verifica que las pruebas de reserva se ejecuten sin errores"""
    resultado = ejecutar_pruebas_reservas()
    assert resultado is True, "Las pruebas de reserva fallaron"
