import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.astroviewer.net/iss/en/")

while True:
    a=driver.find_element_by_xpath("//p[@id='gpt']")
    print(a.text)