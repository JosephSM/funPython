from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.telldunkin.com/')
clickHere = driver.find_element_by_link_text("click here")
print("clicking")
clickHere.click()
