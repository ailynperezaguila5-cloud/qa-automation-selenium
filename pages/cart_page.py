
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    BOTON_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    BOTON_ELIMINAR = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def obtener_cantidad(self):
        contador = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONTADOR_CARRITO)
        )
        return int(contador.text)

    def abrir_carrito(self):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_CARRITO)
        )
        boton.click()
   
    def eliminar_mochila(self):
        boton = WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.BOTON_ELIMINAR)
        )
        boton.click()

    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self.NOMBRE_PRODUCTO)
        return [producto.text for producto in productos]
