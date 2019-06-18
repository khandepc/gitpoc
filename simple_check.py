from  selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec


name_mobile_number="number"
name_radio_button="dataCardType"
xpath_operator="//select[@name='operator']"
xpath_prepaid="//span[contains(text(),'Prepaid')]/preceding-sibling::input"
xpath_circle="//select[@name='circle']"
xpath_proceed_button="//div/button[contains(text(),'Proceed')]"
xpath_amount="//div/input[@name='amount']"

driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.freecharge.in/")

element=driver.find_element_by_name(name_mobile_number)
element.send_keys("8421835355")

element=driver.find_element_by_xpath(xpath_prepaid)
element.click()

element=driver.find_element_by_xpath(xpath_operator)
sel=select.Select(element)
sel.select_by_visible_text("Airtel")

element=driver.find_element_by_xpath(xpath_circle)
sel=select.Select(element)
sel.select_by_visible_text("Maharashtra")

element=driver.find_element_by_xpath(xpath_proceed_button)
element.click()


element=driver.find_element_by_xpath(xpath_amount)
element.send_keys("35")