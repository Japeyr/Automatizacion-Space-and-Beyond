# conftest.py

import pytest
from Planilla_Calculo import head_planilla
import os


@pytest.fixture(scope="session", autouse=True)
def inicializar_reporte_excel():
    """Crea el archivo Excel de reporte al inicio de la sesión de pruebas."""

    # 1. Asegúrate de eliminar cualquier archivo existente para empezar de cero
    if os.path.exists("Casos_Prueba_Space&Beyond.xlsx"):
        os.remove("Casos_Prueba_Space&Beyond.xlsx")

    # 2. Llama a la función para crear el encabezado
    head_planilla()

    # El fixture no necesita retornar nada. Se ejecuta automáticamente (autouse=True).