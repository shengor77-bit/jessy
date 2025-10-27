from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """
    Configura y retorna un driver de Chrome usando selenium-manager.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, username, password):
    """
    Realiza el login en saucedemo.com con las credenciales proporcionadas.
    Espera explícitamente hasta que se redirija a la página de inventario.
    """
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Esperar hasta que se redirija a /inventory.html
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

def add_product_to_cart(driver, product_index=0):
    """
    Añade el producto en la posición especificada (por defecto el primero) al carrito.
    """
    # Encontrar botones de añadir al carrito
    add_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    if product_index < len(add_buttons):
        add_buttons[product_index].click()

def get_cart_count(driver):
    """
    Retorna el número de items en el carrito desde el badge.
    """
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
    except:
        return 0

def navigate_to_cart(driver):
    """
    Navega al carrito de compras.
    """
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

def get_cart_items(driver):
    """
    Retorna una lista de diccionarios con nombre y precio de los items en el carrito.
    """
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    cart_items = []
    for item in items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        cart_items.append({"name": name, "price": price})
    return cart_items