from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 🔐 Datos de acceso
BROWSERSTACK_USERNAME = 'TU_USUARIO'
BROWSERSTACK_ACCESS_KEY = 'TU_CLAVE'

# 📦 Configuración
bstack_options = {
    'os': 'Windows',
    'osVersion': '10',
    'projectName': 'Prueba Múltiple BrowserStack',
    'buildName': 'Build 1',
    'sessionName': 'Pruebas básicas',
    'seleniumVersion': '4.11.0',
    'local': 'false',
    'userName': BROWSERSTACK_USERNAME,
    'accessKey': BROWSERSTACK_ACCESS_KEY
}

options = Options()
options.set_capability('browserName', 'Chrome')
options.set_capability('browserVersion', 'latest')
options.set_capability('bstack:options', bstack_options)

# 🚀 Conexión
driver = webdriver.Remote(
    command_executor='https://hub.browserstack.com/wd/hub',
    options=options
)

try:
    # 1. Validar que Google carga
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("✅ Google abrió correctamente.")

    # 2. Validar que el campo de búsqueda está presente
    search_box = driver.find_element(By.NAME, "q")
    print("✅ Campo de búsqueda encontrado.")

    # 3. Buscar un término
    search_box.send_keys("BrowserStack")
    search_box.submit()
    time.sleep(2)
    assert "BrowserStack" in driver.title
    print("✅ Búsqueda de BrowserStack ejecutada.")

    # 4. Ir a Wikipedia
    driver.get("https://www.wikipedia.org")
    assert "Wikipedia" in driver.title
    print("✅ Wikipedia cargó correctamente.")

    # 5. Buscar texto en Wikipedia (simple validación)
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Selenium (software)")
    search_input.submit()
    time.sleep(2)
    assert "Selenium" in driver.title
    print("✅ Página de Selenium abierta en Wikipedia.")

finally:
    driver.quit()

