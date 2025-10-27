import pytest
from utils.helpers import setup_driver, login, add_product_to_cart, get_cart_count, navigate_to_cart, get_cart_items

@pytest.fixture
def driver():
    """
    Fixture para configurar y cerrar el driver de Selenium.
    """
    driver = setup_driver()
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    """
    Caso de prueba: Interacción con Productos - Añadir al carrito.
    Añade un producto, verifica contador, navega al carrito, comprueba producto.
    """
    login(driver, "standard_user", "secret_sauce")

    # Añadir primer producto
    initial_count = get_cart_count(driver)
    add_product_to_cart(driver, 0)

    # Verificar contador incrementado
    new_count = get_cart_count(driver)
    assert new_count == initial_count + 1

    # Navegar al carrito
    navigate_to_cart(driver)

    # Comprobar producto en carrito
    cart_items = get_cart_items(driver)
    assert len(cart_items) == 1

    # Verificar detalles del producto (asumiendo que coincide con el primero)
    assert cart_items[0]["name"] is not None