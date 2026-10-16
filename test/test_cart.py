
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_anadir_producto_carrito(navegador):
    login = LoginPage(navegador)
    navegador.get("https://www.saucedemo.com/")

    login.iniciar_sesion("standard_user", "secret_sauce")

    inventario = InventoryPage(navegador)
    inventario.anadir_mochila()

    carrito = CartPage(navegador)

    assert carrito.obtener_cantidad() == 1

    carrito.abrir_carrito()

    nombres = carrito.obtener_nombres_productos()

    assert "Sauce Labs Backpack" in nombres

def test_eliminar_producto_carrito(navegador):
    login = LoginPage(navegador)
    navegador.get("https://www.saucedemo.com/")

    login.iniciar_sesion("standard_user", "secret_sauce")

    inventario = InventoryPage(navegador)
    inventario.anadir_mochila()

    carrito = CartPage(navegador)
    carrito.abrir_carrito()

    assert "Sauce Labs Backpack" in carrito.obtener_nombres_productos()

    carrito.eliminar_mochila()

    assert carrito.obtener_nombres_productos() == []
