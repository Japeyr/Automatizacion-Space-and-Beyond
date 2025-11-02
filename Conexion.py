class Conexion:
    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url):
        self.driver.get(url)
        print("Navego a la pagina: ", url)
        self.driver.maximize_window()
