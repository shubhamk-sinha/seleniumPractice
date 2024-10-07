from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep

chrome_properties = Options()
chrome_properties.add_argument("--start-maximized")
chrome_properties.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_properties)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
assert "Practice Page" in driver.title

dropdown = Select(driver.find_element(By.XPATH, '//select[@name="dropdown-class-example"]'))

dropdown.select_by_visible_text("Option2")

dropdown_text = driver.find_element(By.XPATH, '//select[@name="dropdown-class-example"]').text
print(dropdown_text)
assert "Option2" in dropdown_text

dropdown.select_by_index(0)


sleep(3)
driver.quit()