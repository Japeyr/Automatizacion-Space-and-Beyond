import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Login import login
from selenium.webdriver.support import expected_conditions as EC
import re

class planeta:
    def __init__(self, driver):
        self.driver = driver
        self.login_pagina = login(driver)

    def click_planeta(self, elemento_xpath):
        valor = self.driver.find_element(By.XPATH, elemento_xpath)
        valor.click()

    def reservar_planeta(self, name_xpath, email_xpath, social_xpath, phone_xpath, xpath_codigo, xpath_apply,
                         xpath_tilde, name, email, social, phone, descuento_codigo):
        self.limpiar_campos(name_xpath, email_xpath, social_xpath, phone_xpath, xpath_codigo)
        self.driver.find_element(By.XPATH, name_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, email_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, social_xpath).send_keys(social)
        self.driver.find_element(By.XPATH, phone_xpath).send_keys(phone)
        input_file = self.driver.find_element(By.XPATH, "//input[@type='file']")
        self.driver.execute_script("arguments[0].style.display = 'block';", input_file)
        input_file.send_keys("C:/Users/Jorgito/pythonProject/Curso_Selenium/Space&Beyond/Copilot_20250531_124617.png")
        self.driver.find_element(By.XPATH, xpath_codigo).send_keys(descuento_codigo)

        # Esperar hasta que el botón esté habilitado y clickeable
        wait = WebDriverWait(self.driver, 10)
        apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_apply)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", apply_button)
        apply_button.click()

        # Esperar a que aparezca el tilde o confirmación
        tilde = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tilde)))
        tilde.click()

        # self.driver.find_element(By.XPATH, xpath_apply).click()
        # self.driver.find_element(By.XPATH, xpath_tilde).click()
        time.sleep(5)

    def limpiar_campos(self, *xpaths):
        for xpath in xpaths:
            try:
                campo = self.driver.find_element(By.XPATH, xpath)
                campo.clear()
            except Exception as e:
                print(f"No se pudo limpiar el campo {xpath}: {e}")

    def validar_datos(self, nombre, email, seguro_social, telefono, codigo_descuento):
        errores = []

        # --- Validar nombre ---
        if not nombre:
            errores.append("El nombre no puede estar vacío.")
        elif not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$", nombre):
            errores.append("El nombre no debe contener números ni caracteres especiales.")

        # --- Validar email ---
        if not email:
            errores.append("El email no puede estar vacío.")
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            errores.append("El formato del email es inválido.")

        # --- Validar número de seguro social ---
        if not seguro_social:
            errores.append("El número de seguro social no puede estar vacío.")
        elif not re.match(r"^\d{3}-\d{2}-\d{4}$", seguro_social):
            errores.append("El número de seguro social debe tener el formato 123-45-6789.")

        # --- Validar teléfono ---
        if not telefono:
            errores.append("El teléfono no puede estar vacío.")
        else:
            # ------------------------
            # 📱 España: +34 Nxx xxx xxx (N = 6,7,8,9)
            # Ejemplo válido: +34 612 345 678
            patron_espania = r"^\+34\s[6789]\d{2}\s\d{3}\s\d{3}$"

            # ------------------------
            # 🇬🇧 Reino Unido:
            # - Móviles: +44 7xxx xxx xxx
            # - Fijos: +44 1xx xxx xxxx, +44 2x xxxx xxxx, +44 3xx xxx xxxx, etc.
            # Aceptamos espacios o no, pero mantenemos formato legible.
            patron_reino_unido = (
                r"^(\+44\s?7\d{3}\s?\d{3}\s?\d{3}"  # móviles: +44 7xxx xxx xxx
                r"|\+44\s?(1\d{2,4}|2\d|3\d{2})\s?\d{3,4}\s?\d{3,4})$"  # fijos varios formatos
            )

            if re.match(patron_espania, telefono):
                print("✅ Teléfono válido (España).")
            elif re.match(patron_reino_unido, telefono):
                print("✅ Teléfono válido (Reino Unido).")
            else:
                errores.append(
                    "El teléfono debe tener formato español (+34 Nxx xxx xxx, N=6–9) "
                    "o formato británico válido (+44 con prefijo móvil 7 o fijo 1–3)."
                )

        # --- Validar código de descuento ---
        if not codigo_descuento:
            errores.append("El código de descuento no puede estar vacío.")
        else:
            # No permitimos espacios en ningún lugar
            if " " in codigo_descuento:
                errores.append("El código de descuento no puede contener espacios.")
            # Longitud mínima 5 (sin eliminar espacios porque ya se prohíben)
            elif len(codigo_descuento) < 5:
                errores.append("El código de descuento debe tener al menos 5 caracteres.")
            else:
                print("✅ Código válido: el botón 'Apply' debería estar habilitado.")

        # Resultado final
        if errores:
            print("🚫 Errores de validación detectados:")
            for e in errores:
                print("   -", e)
        else:
            print("✅ Todos los datos pasaron las validaciones lógicas.")

        return errores

    # --- Verificación del estado visual del botón Pay now ---
    def verificar_boton_pay(self):
        """
        Comprueba si el botón 'Pay now' está habilitado (amarillo).
        Retorna True si está amarillo, False si sigue gris.
        """
        try:
            boton_pay = self.driver.find_element(By.XPATH, "//button[normalize-space()='Pay now']")
            color = boton_pay.value_of_css_property("background-color")

            if "255, 234, 100" in color or "rgb(255, 234, 100)" in color:
                print("🟡 Botón 'Pay now' habilitado correctamente.")
                return True
            else:
                print(f"⚪ Botón 'Pay now' no habilitado (color actual: {color}).")
                return False

        except Exception as e:
            print(f"⚠️ No se pudo verificar el botón 'Pay now': {e}")
            return False

