from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 🔐 Credenciales de BrowserStack
BROWSERSTACK_USERNAME = 'TU_USUARIO'
BROWSERSTACK_ACCESS_KEY = 'TU_CLAVE'

# 🌐 Configuración remota
bstack_options = {
    'os': 'Windows',
    'osVersion': '10',
    'projectName': 'Proyecto de Graduación',
    'buildName': 'Evaluación BrowserStack',
    'sessionName': '10 pruebas con errores incluidos',
    'seleniumVersion': '4.11.0',
    'local': 'false',
    'userName': BROWSERSTACK_USERNAME,
    'accessKey': BROWSERSTACK_ACCESS_KEY
}

options = Options()
options.set_capability('browserName', 'Chrome')
options.set_capability('browserVersion', 'latest')
options.set_capability('bstack:options', bstack_options)

driver = webdriver.Remote(
    command_executor='https://hub.browserstack.com/wd/hub',
    options=options
)

try:
    # 1. Google carga correctamente
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("✅ Prueba 1: Google cargó correctamente.")

    # 2. Campo de búsqueda está presente
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()
    print("✅ Prueba 2: Campo de búsqueda presente.")

    # 3. Buscar "BrowserStack"
    search_box.send_keys("BrowserStack")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "BrowserStack" in driver.title
    print("✅ Prueba 3: Resultados de búsqueda mostrados.")

    # 4. Click en el primer resultado
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    first_result.click()
    time.sleep(2)
    print("✅ Prueba 4: Click en primer resultado exitoso.")

    # 5. Validar que se abrió BrowserStack
    assert "browserstack.com" in driver.current_url
    print("✅ Prueba 5: Sitio de BrowserStack abierto.")

    # 6. Ir a Wikipedia y validar título
    driver.get("https://www.wikipedia.org")
    assert "Wikipedia" in driver.title
    print("✅ Prueba 6: Wikipedia cargó correctamente.")

    # 7. Buscar "Selenium (software)"
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Selenium (software)")
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Selenium" in driver.title
    print("✅ Prueba 7: Página de Selenium abierta.")

    # 8. Validar contenido en la página
    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "automated testing" in body_text
    print("✅ Prueba 8: Contenido validado en Selenium.")

    # ⚠️ 9. ERROR INTENCIONAL: Buscar un elemento que no existe
    print("⚠️  Prueba 9: Buscando elemento inexistente (debe fallar)...")
    driver.find_element(By.ID, "este_elemento_no_existe")  # Provocará error

    # ⚠️ 10. ERROR INTENCIONAL: Validar título incorrecto
    print("⚠️  Prueba 10: Validando título equivocado (debe fallar)...")
    assert "EstoNoExisteEnElTitulo" in driver.title  # Provocará error

except Exception as e:
    print(f"❌ Error detectado durante la ejecución: {e}")
finally:
    driver.quit()
