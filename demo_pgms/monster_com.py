import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.monsterindia.com/")
driver.maximize_window()


#to find "pyhton" job deatils

'''driver.find_element_by_id("wzrk-cancel").click()
driver.find_element_by_id("SE_home_autocomplete").send_keys("Python")
driver.find_element_by_xpath('//input[@class="btn"]').click()

job_details_all_links=driver.find_elements_by_xpath('//div[@class="job-tittle"]/h3/a')
for links_titles in job_details_all_links:
    print(links_titles.text)'''

#to find all links text----> footer

'''driver.find_element_by_id("wzrk-cancel").click()
footer_links=driver.find_elements_by_xpath('//div[@id="seo-fdata"]//a')

for links in footer_links:
    print(links.text)'''

