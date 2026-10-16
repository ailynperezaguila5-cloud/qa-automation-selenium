from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def iniciar_sesion(self, usuario, password):

        campo_usuario = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAMPO_USUARIO)
        )
        campo_usuario.send_keys(usuario)

        campo_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAMPO_PASSWORD)
        )
        campo_password.send_keys(password)

        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_LOGIN)
        )
        boton.click()
    def obtener_mensaje_error(self):
        mensaje = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MENSAJE_ERROR)
        )
        return mensaje.text