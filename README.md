
# Portfolio de QA Automation — Selenium y Python

## Descripción del proyecto

Proyecto de automatización de pruebas web utilizando Python, Selenium WebDriver y pytest.

Se utiliza SauceDemo, una aplicación de comercio electrónico de demostración, para practicar pruebas funcionales automatizadas de la interfaz web.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- Esperas explícitas
- Fixtures y aserciones de pytest

## Casos de prueba automatizados

1. Inicio de sesión correcto con credenciales válidas.
2. Inicio de sesión incorrecto con credenciales inválidas.
3. Verificación del catálogo de productos.
4. Añadir un producto al carrito.
5. Comprobar que el producto aparece en el carrito.
6. Eliminar un producto del carrito.
7. Verificar que el carrito queda vacío después de eliminar el producto.

## Estructura del proyecto

- `pages/`: clases que representan las páginas de la aplicación.
- `test/`: pruebas automatizadas.
- `conftest.py`: configuración compartida y fixture del navegador.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Instalación

Clonar o descargar el repositorio y acceder a la carpeta del proyecto.

Instalar las dependencias con el siguiente comando:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Para ejecutar toda la suite de pruebas:

```bash
python -m pytest
```

Para ver los nombres de las pruebas y sus resultados detallados:

```bash
python -m pytest -v
```

## Resultados

Durante el desarrollo se han ejecutado satisfactoriamente las pruebas automatizadas en el entorno local.

Para consultar los resultados actuales, ejecutar la suite con pytest.

## Objetivo del proyecto

Demostrar conocimientos prácticos de automatización de pruebas web, localización de elementos, esperas explícitas, validaciones mediante aserciones, gestión del navegador con fixtures y organización del código mediante Page Object Model.

## Autora

QA Tester | Python | Selenium | pytest | ISTQB CTFL 4.0
