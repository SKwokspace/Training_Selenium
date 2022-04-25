import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()

driver.find_element_by_link_text("Books").click()
element=driver.find_element_by_id("products-orderby")
s=Select(element)
s.select_by_visible_text("Price: Low to High")
sleep(5)
s.select_by_visible_index(3)
s.select_by_visible_value("onchange")