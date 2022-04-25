import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.ajio.com/")

driver.find_element_by_css_selector("input[placeholder='Search AJIO']").send_keys("joggers")
driver.find_element_by_css_selector("span[class='ic-search']").click()

ele=driver.find_element_by_xpath("//div[@class='filter-dropdown']/..//select")
s = Select(ele)
s.select_by_visible_text("Price (highest first)")
# details=driver.find_element_by_class_name("contentHolder")
details = driver.find_elements_by_xpath("//div[@class='contentHolder']")
# print(details)
c=0
n=2
for product in details:
    c += 1
    if c <= n:
        print(product.text)
