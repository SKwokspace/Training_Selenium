import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()

import csv

path = r"C:\Users\MohanMadhuri\PycharmProjects\My_Selenium\demo\validate_csv.csv"


def read_csv():
    with open("validate_csv.csv") as file:
        rows = csv.reader(file)
        headers = next(rows)

        # for row in rows:
        #   print(row)

        expected_prices = {row[0]: float(row[1]) for row in rows}
        # return expected_prices
        print(expected_prices)


expected_prices = read_csv()

# for item,expected_price in expected_prices:
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()

# a=driver.find_elements_by_xpath("//div[@class='product-grid home-page-product-grid']//h2//a
#                                 "//a[text()='$25 Virtual Gift Card']/../..//span[@class='price actual-price']").text


# a=driver.find_elements_by_xpath("//div[@class='product-grid home-page-product-grid']//h2//a//").text

# a=driver.find_elements_by_xpath("//a[text()='$25 Virtual Gift Card']/../..//span[@class='price actual-price']").text
# print(a)

products = driver.find_elements_by_xpath("//div[@class='details']//a")
for product in products:
    print(product.text)

prices = driver.find_elements_by_xpath("//span[@class='price actual-price']")
for price in prices:
    print(price.text)

