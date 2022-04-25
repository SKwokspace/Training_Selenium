import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.python.org/downloads/")
driver.find_element_by_xpath("//a[text()='Python 3.9.12']/../..//a[text()='Release Notes']")