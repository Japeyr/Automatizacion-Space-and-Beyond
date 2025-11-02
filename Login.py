from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os

class login:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self, elemento_xpath):
        val = self.driver.find_element(By.XPATH, elemento_xpath)
        val.click()
        print("Se hizo click en el botón")

    def insertar_user(self, elemento_path, user):
        texto1 = self.driver.find_element(By.XPATH, elemento_path)
        texto1.send_keys(user)
        texto1.send_keys(Keys.TAB)

    def insetar_pass(self, elemento_path, password):
        texto2 = self.driver.find_element(By.XPATH, elemento_path)
        texto2.send_keys(password)

    def loguearse(self, elemento_path):
        val = self.driver.find_element(By.XPATH, elemento_path)
        val.click()

    def validar_login(self):
        try:
            ingreso = self.driver.find_element(By.XPATH, "//span[normalize-space()='Hello, John']")
            return ingreso.is_displayed()
        except NoSuchElementException:
            return False

    def logout(self):
        try:
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Hello, John']").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Log out']").click()
            print("🔓 Logout ejecutado")
        except NoSuchElementException:
            print("⚠️ No se encontró el botón de logout")

    def validar_logout(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@class='NavButton__nav-button___34wHC']")
            print("✅ Logout exitoso: volvió al login")
            return True
        except NoSuchElementException:
            print("❌ Logout fallido")
            return False

    @staticmethod
    def es_usuario_valido(user):
        return user.isalpha() and " " not in user

    @staticmethod
    def es_password_robusta(password):
        return (
                len(password) >= 8 and
                password.isalpha() and " " not in password and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()" for c in password)
        )

    @staticmethod
    def guardar_resultado(contenido, archivo):
        os.makedirs("output", exist_ok=True)  # Crea la carpeta si no existe
        ruta = f"output/{archivo}"
        with open(ruta, "a", encoding="utf-8") as file:
            file.write(contenido + "\n")
            print(f"Resultado guardado en {archivo}")
