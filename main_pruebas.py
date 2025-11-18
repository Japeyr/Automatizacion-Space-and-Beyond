import glob
import os
import time
from itertools import product
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Conexion import Conexion
from Login import login
from Planilla_Calculo import head_planilla, datos1, datos2, datos3


# -------------------------- Función auxiliar de clic seguro --------------------------
def safe_click(driver, xpath, timeout=10):
    try:
        boton = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton)
        time.sleep(0.5)
        boton.click()
    except ElementClickInterceptedException:
        print("Alerta! Elemento bloqueado, intentando con JavaScript...")
        driver.execute_script("arguments[0].click();", boton)
    except (TimeoutException, ElementNotInteractableException) as e:
        print(f" No se pudo hacer clic: {e}")
        raise e


# -------------------------- Función que prueba cada planeta --------------------------
def test_probar_planeta(index_planeta, xpath_reserva, combinaciones):
    from selenium import webdriver
    from Conexion import Conexion
    from Reserva import planeta
    import time

    print(f"\n Iniciando pruebas para planeta {index_planeta + 1}")
    driver = webdriver.Chrome()
    conexion = Conexion(driver)
    conexion.navegar("https://demo.testim.io/")
    destino = planeta(driver)

    xpath_login_button = "//button[@class='NavButton__nav-button___34wHC']"
    xpath_user = "//div[@class='Box__box___2XzJ2 Login__card___32Upz']//div[1]//input[1]"
    xpath_pass = "//input[@type='password']"
    xpath_submit = "//button[@type='submit']"
    xpath_more_button = "//button[normalize-space()='Load more']"

    destino.login_pagina.click_login(xpath_login_button)
    destino.login_pagina.insertar_user(xpath_user, "Jorge")
    destino.login_pagina.insetar_pass(xpath_pass, "jpai19aegA58")
    destino.login_pagina.loguearse(xpath_submit)
    destino.login_pagina.loguearse(xpath_more_button)
    time.sleep(4)

    xpath_name = "//form//div[1]//input[1]"
    xpath_email = "//input[@type='email']"
    xpath_social = "//body//div[@id='app']//div//div//div[@class='flexboxgrid__row___1y_mg flexboxgrid__center-xs___1JWon']//div[3]//input[1]"
    xpath_phone = "//input[@type='tel']"
    xpath_code = "//input[@name='promo']"
    xpath_apply = "//button[normalize-space()='Apply']"
    xpath_tilde = "//div[@class='theme__check___2B20W']"

    os.makedirs("output", exist_ok=True)
    archivo_temp = f"output/resultados_planeta_{index_planeta + 1}.txt"

    with open(archivo_temp, "w", encoding="utf-8") as f:
        for j, (n, e, s, t, c) in enumerate(combinaciones, start=1):
            print(f"    Planeta {index_planeta + 1}, Prueba {j}: {n}, {e}, {s}, {t}, {c}")
            resultado_validacion_logica = "OK"
            resultado_web = "OK"

            try:
                safe_click(driver, xpath_reserva)
                time.sleep(2)

                errores = destino.validar_datos(n, e, s, t, c)
                if errores:
                    resultado_validacion_logica = "FALLÓ_LOGICA"
                    f.write(f"{index_planeta+1};{n};{e};{s};{t};{c};{resultado_validacion_logica};{resultado_web}\n")
                    driver.back()
                    time.sleep(2)
                    continue

                destino.reservar_planeta(xpath_name, xpath_email, xpath_social, xpath_phone,
                                         xpath_code, xpath_apply, xpath_tilde, n, e, s, t, c)
                time.sleep(3)

                if not destino.verificar_boton_pay():
                    resultado_web = "FALLÓ_WEB"

                f.write(f"{index_planeta+1};{n};{e};{s};{t};{c};{resultado_validacion_logica};{resultado_web}\n")
                driver.back()
                time.sleep(3)

            except Exception as ex:
                print(f"Alerta! Error en planeta {index_planeta + 1}, prueba {j}: {ex}")
                f.write(f"{index_planeta+1};{n};{e};{s};{t};{c};ERROR;ERROR\n")
                try:
                    driver.back()
                    time.sleep(2)
                except:
                    pass

    driver.quit()
    print(f"OK Finalizó planeta {index_planeta + 1}. Resultados guardados en {archivo_temp}")


# -------------------------- Función para ejecutar pruebas de login --------------------------
def ejecutar_pruebas_login():
    fila_logout = 12
    escenarios = [
        {"user": "Jorge", "pass": "agfgadfg", "esperado": True},
        {"user": "", "pass": "agfgadfg", "esperado": False},
        {"user": "Jorge", "pass": "", "esperado": False},
        {"user": "", "pass": "", "esperado": False},
        {"user": "Jorge123", "pass": "agfgadfg", "esperado": False},
    ]

    xpath_login_button = "//button[@class='NavButton__nav-button___34wHC']"
    xpath_user = "//div[@class='Box__box___2XzJ2 Login__card___32Upz']//div[1]//input[1]"
    xpath_pass = "//input[@type='password']"
    xpath_submit = "//button[@type='submit']"

    fallaron_todos = True
    resultados = []
    resultados_logout = []

    for i, caso in enumerate(escenarios, start=1):
        driver = None
        try:
            driver = webdriver.Chrome()
            conexion = Conexion(driver)
            conexion.navegar("https://demo.testim.io/")
            login_pagina = login(driver)

            login_pagina.click_login(xpath_login_button)
            login_pagina.insertar_user(xpath_user, caso["user"])
            login_pagina.insetar_pass(xpath_pass, caso["pass"])
            login_pagina.loguearse(xpath_submit)
            time.sleep(3)
            resultado = login_pagina.validar_login()

            # --------------------------- LÓGICA AGREGADA (datos1) ---------------------------
            # Determinar si el resultado coincide con lo esperado para escribir en Excel
            resultado_flag = "esperado" if resultado == caso["esperado"] else "no_esperado"
            datos1(i, caso["user"], caso["pass"], resultado_flag)
            # --------------------------------------------------------------------------------

            if resultado == caso["esperado"]:
                fallaron_todos = False
                resultados.append((i, "OK"))
            else:
                resultados.append((i, "FALLÓ"))

        except Exception as e:
            resultados.append((i, f"ERROR: {e}"))
        finally:
            if driver:
                driver.quit()

    if fallaron_todos:
        raise Exception(" Ningún escenario se comportó como se esperaba.")
    return resultados


# -------------------------- Función para ejecutar pruebas de reserva --------------------------
def ejecutar_pruebas_reservas():
    nombre = ["Jorge", "Jorge123", ""]
    email = ["peyrano@gmail.com", "peyrano", ""]
    seguro_social = ["123-45-6789", "1234-56-789", ""]
    telefono = ["+34 612 345 678", "+34 lkj 345 678", ""]
    codigo_descuento = ["ASDF34", "ASDF 34", ""]

    combinaciones = list(product(nombre, email, seguro_social, telefono, codigo_descuento))
    xpath_reserva = [
        "//div[@class='Box__box___2XzJ2 Gallery__items-box___2hOZl']//div[1]//div[4]//button[1]",
        "//div[2]//div[4]//button[1]",
        "//div[3]//div[4]//button[1]",
        "//div[@class='flexboxgrid__row___1y_mg flexboxgrid__center-xs___1JWon']//div[4]//div[4]//button[1]",
        "//div[5]//div[4]//button[1]",
        "//div[6]//div[4]//button[1]",
        "//div[7]//div[4]//button[1]",
        "//div[8]//div[4]//button[1]",
        "//div[9]//div[4]//button[1]"
    ]

    with Pool(processes=3) as pool:
        pool.starmap(test_probar_planeta, [(i, xpath_reserva[i], combinaciones) for i in range(len(xpath_reserva))])

        # --------------------------- LÓGICA AGREGADA (Consolidación con datos3) ---------------------------
        print("\n📦 Consolidando resultados en Excel...")

        # Combinar resultados de todos los archivos temporales
        for archivo in glob.glob("output/resultados_planeta_*.txt"):
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        # El formato de la línea es: planeta_num;n;e;s;t;c;r_log;r_web
                        planeta_num, n, e, s, t, c, r_log, r_web = linea.strip().split(";")
                        # Llama a datos3 para escribir en la planilla Excel
                        datos3(0, planeta_num, n, e, s, t, c, r_log, r_web)
                    except Exception as e:
                        print(f"Alerta! Error al procesar la línea en el archivo {archivo}: {e}")
            # Opcional: Eliminar el archivo temporal después de procesar
            # os.remove(archivo)
            # ---------------------------------------------------------------------------------------------------
        return True  # <--- Ahora el return True va después de la consolidación
