import os
from selenium import webdriver

desired_cap = {
    'browserName': 'Chrome',
    'browserVersion': 'latest',
    'bstack:options': {
        'os': 'Windows',
        'osVersion': '10',
        'projectName': 'Prueba BrowserStack',
        'buildName': 'Build 1',
        'sessionName': 'Validar título Google',
        'local': 'false',
        'seleniumVersion': '4.0.0',
        'userName': os.environ.get('BROWSERSTACK_USERNAME'),
        'accessKey': os.environ.get('BROWSERSTACK_ACCESS_KEY')
    }
}

driver = webdriver.Remote(
    command_executor='https://hub.browserstack.com/wd/hub',
    desired_capabilities=desired_cap
)

driver.get("https://www.google.com")
assert "Google" in driver.title
driver.quit()
