import time
import re
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")

# get all elements link
element_items = driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")

# get all elements link text
all_elements = [item.text for item in element_items]

# get all elements price
element_prices = driver.find_elements_by_xpath("//span[@class='art-price']")

# get all elements price text
a = [item.text for item in element_prices]

# get all elements price text in float form and add to list
all_prices=[]
for item in a:
    actual_prices = float("".join(re.findall(r"[\d\.]", item)))
    all_prices.append(actual_prices)
print(all_prices)

#put all elemts and prices in dict form
actual_prices={}
for product,price in zip(all_elements,all_prices):
    actual_prices[product]=price
print(actual_prices)
    
#print value less than 100
less_100 = {product:price for product,price in actual_prices.items() if price<100}
print(less_100)


# print(element_prices)
# for prices in element_prices:
#     print(prices.text)
