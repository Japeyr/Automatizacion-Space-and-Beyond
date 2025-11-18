# 🪐 Automatización de Pruebas Funcionales – Space&Beyond

Este proyecto implementa una **automatización de pruebas funcionales** sobre el sitio [demo.testim.io](https://demo.testim.io/), utilizando **Python y Selenium WebDriver**.  
El sistema verifica los flujos de **login/logout** y **reserva de planetas**, aplicando validaciones lógicas, criterios de partición de equivalencias y valores límite.  
Los resultados se registran automáticamente tanto en **archivos Excel** como en **archivos `.txt`**, generando un reporte estructurado y visualmente claro.

---

## ⚙️ Tecnologías y librerías utilizadas

- **Lenguaje:** Python 3  
- **Framework principal:** Selenium WebDriver  
- **Manejo de Excel:** openpyxl  
- **Automatización concurrente:** multiprocessing  
- **Gestión de rutas y archivos:** os, glob, time  
- **Expresiones regulares:** re  
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

## 📁 Estructura del proyecto

```bash
SpaceBeyond-Automation/
│
├── Conexion.py              # Controla la conexión y navegación del navegador
├── Login.py                 # Lógica de login, logout y validaciones de credenciales
├── Reserva.py               # Automatización del formulario de reserva de planetas
├── Planilla_Calculo.py      # Genera reportes en Excel con formato y fecha
├── Ejecucion.py             # Orquestador principal: ejecuta login y reservas en paralelo
│
├── output/                  # Carpeta generada automáticamente con resultados
│   ├── resultados_login.txt
│   ├── resultados_planeta_X.txt
│   └── Casos_Prueba_Space&Beyond.xlsx
│
├── Copilot_20250531_124617.png   # Imagen utilizada en el formulario (archivo de prueba)
└── README.md
```

---

## 🚀 Uso del script

1. Ejecutar el archivo principal
python Ejecucion.py

2. El script realiza dos etapas:
   🧩 Pruebas de Login y Logout:
Ejecuta escenarios con distintas combinaciones de usuario y contraseña, validando comportamientos esperados.
Los resultados se registran directamente en Excel y (opcionalmente) en output/resultados_login.txt.

🪐 Pruebas de Reserva de Planetas:
Genera automáticamente 243 combinaciones de prueba (valores válidos e inválidos), aplicando validaciones lógicas y visuales.
Las reservas se ejecutan en paralelo (3 procesos simultáneos) para optimizar el tiempo de ejecución.
Los resultados parciales se guardan en archivos .txt y luego se consolidan en el Excel final.

3. Reporte final:
Al completar la ejecución, se genera el archivo:

output/Casos_Prueba_Space&Beyond.xlsx
con los resultados formateados, fecha, tester y estado de cada caso.

---

## 🧠 Conceptos aplicados

- Encapsulamiento y responsabilidad única

- Multiprocesamiento para ejecución concurrente

- Validaciones con expresiones regulares

- Partición de equivalencias y valores límite

- Generación automática de reportes

- Manejo de errores y tolerancia a fallos de interacción

---

## 🧑‍💻 Autor

Jorge Peyrano

QA Manual & Automation | Python | Selenium | Testing Funcional

📎 [Linkedin](www.linkedin.com/in/jorge-peyrano) | [GitHub](https://github.com/Japeyr)
