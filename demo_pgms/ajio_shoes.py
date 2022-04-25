import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.ajio.com/")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_css_selector("input[placeholder='Search AJIO']").send_keys("shoes")
driver.find_element_by_css_selector("span[class='ic-search']").click()

# driver.find_elements_by_xpath("//input[@name='searchVal']").click()
# driver.find_elements_by_xpath("//span[text()='shoes']").click()
sort_ = driver.find_element_by_xpath("//div[@class='filter-dropdown']/..//select")
s = Select(sort_)
s.select_by_visible_text("Price (highest first)")
products = driver.find_elements_by_xpath("//div[@class='contentHolder']")

count_ = 0
n = 6

for product in products:
    count_ += 1
    if count_ <= n:
        print(product.text)
