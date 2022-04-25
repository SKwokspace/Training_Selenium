import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get(r"C:\Users\MohanMadhuri\Downloads\demo.html")

a =driver.find_element_by_id("Standard_cars")
b = Select(a)
b.select_by_visible_text("Audi")
time.sleep(5)
b.select_by_index(5)
time.sleep(5)
# file:///C:/Users/MohanMadhuri/Downloads/TYS/Selenium/demo-html-20220416
#
#
# # s = Select(ele)
# # s.select_by_visible_text("Audi")
# # items = s.options
# # data = [item.text for item in items]
# #
# for item in items:
#     data.append(item.text)
#     for item in data:
#         print(item)
