import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.helpers import setup_driver, login

@pytest.fixture
def driver():
    """
    Fixture para configurar y cerrar el driver de Selenium.
    """
    driver = setup_driver()
    yield driver
    driver.quit()

def test_login_successful(driver):
    """
    Caso de prueba: Automatización de Login.
    Navega a login, ingresa credenciales válidas, valida redirección a inventario.
    """
    login(driver, "standard_user", "secret_sauce")

    # Validar título y presencia de productos
    assert "Products" in driver.title or "Swag Labs" in driver.title
    assert "/inventory.html" in driver.current_url

    # Validar presencia de productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0

    # Listar nombre y precio del primero
    first_product = products[0]
    name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {name} - {price}")