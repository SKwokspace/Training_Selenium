from selenium.webdriver import Chrome
driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
driver.get("https://www.chess.com/")

driver.find_element_by_link_text("https://www.chess.com/play/computer").click()