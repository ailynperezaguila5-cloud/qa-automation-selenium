
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    TITULO = (By.CLASS_NAME, "title")
    BOTON_MOCHILA = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        titulo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITULO)
        )
        return titulo.text

    def contar_productos(self):
        productos = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCTOS)
        )
        return len(productos)

    def anadir_mochila(self):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_MOCHILA)
        )
        boton.click()

