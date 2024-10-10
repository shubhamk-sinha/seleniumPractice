from time import sleep
from driverInitialization import Driverinitialization as DI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = DI.chrome_driver

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkbox = driver.find_element(By.XPATH, '//input[@value="option2"]')

wait = WebDriverWait(driver, 5)
wait.until(ec.visibility_of(checkbox))

assert not checkbox.is_selected()

checkbox.click()

assert checkbox.is_selected()

sleep(3)
driver.quit()
