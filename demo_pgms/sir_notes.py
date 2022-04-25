import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("file:///C:/Users/MohanMadhuri/Desktop/training/demo.html")
driver.maximize_window()

languages = ['Ruby', 'Java', 'Python', 'C#', 'JavaScript']

for language in languages:

    _xpath = f"//td[text='{language}']/..//input[@name='download']"
    driver.find_element_by_xpath(_xpath).click()
