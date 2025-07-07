from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ✅ Datos de acceso
BROWSERSTACK_USERNAME = 'kardhidem_QrP5u4'
BROWSERSTACK_ACCESS_KEY = 'qFxQwJxqHWAyXHABR9S7'

# ✅ Capabilities
bstack_options = {
    'os': 'Windows',
    'osVersion': '10',
    'projectName': 'Prueba BrowserStack',
    'buildName': 'Build 1',
    'sessionName': 'Validar título Google',
    'seleniumVersion': '4.11.0',
    'local': 'false',
    'userName': BROWSERSTACK_USERNAME,
    'accessKey': BROWSERSTACK_ACCESS_KEY
}

options = Options()
options.set_capability('browserName', 'Chrome')
options.set_capability('browserVersion', 'latest')
options.set_capability('bstack:options', bstack_options)

# ✅ Ejecutar prueba
driver = webdriver.Remote(
    command_executor='https://hub.browserstack.com/wd/hub',
    options=options
)

driver.get("https://www.google.com")
assert "Google" in driver.title
driver.quit()
