import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.goibibo.com/")

driver.find_element_by_xpath("//span[@class='footer-sprite twitterIcon']").click()
handles=driver.window_handles

driver.switch_to.window([handles[1]])
driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hi")


'''driver.find_element_by_xpath("//span[text()='Departure']").click()
driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
driver.find_element_by_xpath("//div[text()='June 2022']/../..//div[@aria-label='Wed Jun 15 2022']").click()'''