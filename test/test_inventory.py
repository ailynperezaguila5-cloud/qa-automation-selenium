
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_catalogo_productos(navegador):
    login = LoginPage(navegador)
    navegador.get("https://www.saucedemo.com/")

    login.iniciar_sesion("standard_user", "secret_sauce")

    inventario = InventoryPage(navegador)

    assert inventario.obtener_titulo() == "Products"
    assert inventario.contar_productos() > 0
