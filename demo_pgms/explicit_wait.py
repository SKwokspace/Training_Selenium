import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement


class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        return result



def wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]

        wait = WebDriverWait(driver, 5)
        v = _visibility_of_element_located(locator)
        wait.until(v)

        return func(*args, **kwargs)

    return wrapper


@wait
def enter_text(locator, *, value):
    driver.find_element(*locator).send_keys(value)


@wait
def click_element(locator):
    driver.find_element(*locator).click()


@wait
def select_item():
    ...


driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()

click_element(("link text", "Register"))
click_element(("id", "gender-male"))
enter_text(("id", "FirstName"), value="hello")
