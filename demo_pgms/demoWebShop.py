import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

# driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
# driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()

# register form
'''driver.find_element_by_class_name("ico-register").click()
time.sleep(2)

driver.find_element_by_id("gender-female").click()
driver.find_element_by_id("FirstName").send_keys("shwetha")
driver.find_element_by_id("LastName").send_keys("shwetha")
driver.find_element_by_id("Email").send_keys("swetha@mail.com")
driver.find_element_by_id("Password").send_keys("shwetha")
driver.find_element_by_id("ConfirmPassword").send_keys("shwetha")
driver.find_element_by_id("register-button").click()
driver.find_element_by_class_name("button-1 register-continue-button").click()'''

'''driver.find_element_by_link_text("Books").click()
element = driver.find_element_by_id("products-orderby")
s = Select(element)
s.select_by_visible_text("Price: Low to High")'''

'''# time.sleep(5)
# s.select_by_index(2)
# time.sleep(5)
# s.select_by_value("http://demowebshop.tricentis.com/books?orderby=15")'''

# list of all the option inside the list
'''
items = s.options
data = [item.text for item in items]

for item in items:n 
    data.append(item.text)
for item in data:
    print(item)'''

# to check whether element present in the list
'''
items = s.options
data = [item.text for item in items]
for index,item in enumerate(data):
    if item=="Created on":
        s.select_by_visible_text(item)
        print(item,index)

'''

# validate all
'''expected_prices={"$25 Virtual Gift Card":25.00,"14.1-inch Laptop":1590.00}

for product,expected_price in expected_prices.items():
    _xpath=f"//a[text()='{product}']/../..//span[@class='price actual-price']"
    actual_price=driver.find_element_by_xpath(_xpath).text
    print(actual_price)

    if float(actual_price) == expected_price:
        print("pass")

    else:
        print("fail")'''


driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()

class _visibility_of_element_located(visibility_of_element_located):
    # def __init__(self,locator):
    #     super().__init__(locator)

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
def cselect_item():
    ...



click_element(("link text", "Register"))
click_element(("id", "gender-male"))
enter_text(("id", "FirstName"), value="hello")
