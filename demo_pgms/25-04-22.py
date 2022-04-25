import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


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
        instance = args[0]
        locator = args[1]

        wait = WebDriverWait(instance.driver, 5)
        v = _visibility_of_element_located(locator)
        wait.until(v)

        return func(*args, **kwargs)

    return wrapper


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self, locator, *, value):
        driver.find_element(*locator).send_keys(value)

    @wait
    def click_element(self, locator):
        driver.find_element(*locator).click()

    @wait
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError(f"invalid Type {item}")

    @wait
    def select_items(self, locator, *, items):
        for _item in items:
            try:
                self.select_item(locator, item=_item)

            except NoSuchElementException:
                print(f"could not find item {_item}")
                continue


driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')

driver.get(r"C:\Users\MohanMadhuri\Desktop\training\demo.html")
driver.maximize_window()
time.sleep(5)

s = SeleniumWrapper(driver)

s.select_items(("id", "multiple_cars"), items=['Audi', 'BMW', 'Ford'])
