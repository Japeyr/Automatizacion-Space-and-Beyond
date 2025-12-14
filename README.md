# 🪐 Automatización de Pruebas Funcionales – Space&Beyond

Este proyecto implementa una **automatización de pruebas funcionales** sobre el sitio [demo.testim.io](https://demo.testim.io/), utilizando **Python, Selenium WebDriver**, y el framework de testing **Pytest**.  
El objetivo es validar de forma automatizada los flujos críticos de login / logout y reserva de planetas, aplicando criterios de partición de equivalencias, valores límite y validaciones funcionales reales.

Las pruebas se ejecutan como un flujo completo, simulando el comportamiento de un usuario final, y los resultados se registran automáticamente en archivos Excel formateados y archivos de texto.

---

## ⚙️ Tecnologías y librerías utilizadas

- **Lenguaje:** Python 3.12
- **Framework de Testing:** Pytest 
- **Framework principal:** Selenium WebDriver  
- **Manejo de Excel:** openpyxl  
- **Ejecución concurrente:** multiprocessing  
- **Gestión de rutas y archivos:** os, glob, time  
- **Validaciones:** Expresiones Regulares (re)  
- **Entorno de ejecución:** Google Chrome + ChromeDriver  

---

## 💻 Instalación y configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/SpaceBeyond-Automation.git
   cd SpaceBeyond-Automation
   ```

2. **Crear entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ``` 

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar ChromeDriver**
   Descargá la versión compatible con tu navegador desde https://chromedriver.chromium.org/downloads

   Agregá el ejecutable de chromedriver a tu PATH o colocalo en el directorio del proyecto.
   
---

## 📁 Estructura del proyecto (Actualizado)

```bash
SpaceBeyond-Automation/
│
├── ejecucion.py # Script principal que ejecuta el flujo completo E2E
├── test_ejecucion.py # Test Pytest que ejecuta ejecucion.py como script real
│
├── Conexion.py # Inicialización y control del navegador
├── Login.py # Lógica de login, logout y validaciones
├── Reserva.py # Automatización del formulario de reservas
├── Planilla_Calculo.py # Generación del reporte Excel con openpyxl
│
├── output/ # Resultados generados automáticamente
│ ├── resultados_login.txt
│ ├── resultados_planeta_X.txt
│ └── Casos_Prueba_Space&Beyond.xlsx
│
├── pytest.ini # Configuración de Pytest
├── requirements.txt
└── README.md
```

---

## 🚀 Uso del script

### Usando Ejecucion.py (python Ejecucion.py)

Este modo ejecuta el flujo completo:

- Limpieza de archivos previos

- Pruebas de login y logout

- Pruebas de reservas con múltiples combinaciones

- Ejecución concurrente de escenarios

- Generación del reporte Excel final


### Usando pytest (pytest -v - Recomendado)

En este modo:

- Pytest ejecuta test_ejecucion.py

- El test lanza ejecucion.py como si fuera terminal o PyCharm

- Se valida que todo el flujo termine correctamente

- Se detectan fallos reales del proceso completo

- Este enfoque simula un test E2E real, ideal para CI/CD. 

---

## Flujo de pruebas automatizadas
### 1. Login / Logout

- Ejecución de múltiples combinaciones de usuario y contraseña

- Casos válidos e inválidos

- Registro de resultados en Excel y archivos .txt

### 2. Reserva de planetas

- Generación automática de combinaciones de prueba

- Validación de campos obligatorios y valores inválidos

- Ejecución en paralelo para optimizar tiempos

- Consolidación de resultados en el reporte final

---

## 🧠 Conceptos aplicados

- Testing end‑to‑end con Pytest

- Automatización web con Selenium

- Separación de responsabilidades por módulo

- Multiprocessing aplicado a testing

- Manejo de errores y tolerancia a fallos

- Generación automática de evidencias

- Diseño orientado a entornos CI/CD

---

## 🧑‍💻 Autor

Jorge Peyrano

QA Manual & Automation | Python | Selenium | Testing Funcional

📎 [Linkedin](www.linkedin.com/in/jorge-peyrano) | [GitHub](https://github.com/Japeyr)
