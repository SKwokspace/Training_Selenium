from selenium.webdriver import Chrome
driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://testautomationpractice.blogspot.com/")


driver.find_element_by_id('RESULT_TextField-1').send_keys("firstname")
driver.find_element_by_id('RESULT_TextField-2').send_keys("secondname")
driver.find_element_by_id('RESULT_TextField-3').send_keys("9874561230")
driver.find_element_by_id('RESULT_TextField-4').send_keys("INDIA")
driver.find_element_by_id('RESULT_TextField-5').send_keys("Bangalore")
driver.find_element_by_id('RESULT_RadioButton-7_1').click()
driver.find_element_by_id('RESULT_CheckBox-8_0').click()
