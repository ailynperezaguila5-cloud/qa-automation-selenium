from pages.login_page import LoginPage

def test_login(navegador):
    login = LoginPage(navegador)

    navegador.get("https://www.saucedemo.com/")

    login.iniciar_sesion("standard_user", "secret_sauce")

    assert "/inventory.html" in navegador.current_url

def test_login_incorrecto(navegador):
    login = LoginPage(navegador)
    navegador.get("https://www.saucedemo.com/")

    login.iniciar_sesion("standard_user", "ERROR")

    mensaje = login.obtener_mensaje_error()

    assert "Username and password do not match" in mensaje
    assert "/inventory.html" not in navegador.current_url