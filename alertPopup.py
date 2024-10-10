from driverInitialization import Driverinitialization as DI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

alert_ele = '//input[@placeholder="Enter Your Name"]'
name = "Harsh"
alert_text = f"Hello {name}, share this practice page and share your knowledge"
alert_btn = 'following-sibling::input[@value="Alert"]'
confirm_alert_btn = 'following-sibling::input[@value="Confirm"]'
confirm_alert_txt = f"Hello {name}, Are you sure you want to confirm?"

driver = DI.chrome_driver
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

alert_input = driver.find_element(By.XPATH, alert_ele)

# Handling Alert having only "OK" button by using accept() method
wait.until(ec.visibility_of(alert_input))
alert_input.send_keys(name)

""" Below used XPATH-element-chaining, i.e., 
    used one XPATH element (alert_input) to find another element instead of searching in entire HTML POM
    using driver.find_element()
"""
alert_input.find_element(By.XPATH, alert_btn).click()
alert_wind = driver.switch_to.alert
assert alert_wind.text == alert_text
sleep(1)
alert_wind.accept()

sleep(1)

# Handling Alert by clicking on "Ok" button using accept() method
alert_input.send_keys(name)
alert_input.find_element(By.XPATH, confirm_alert_btn).click()
confirm_alert_wind = driver.switch_to.alert
assert confirm_alert_wind.text == confirm_alert_txt
sleep(1)
confirm_alert_wind.accept()

sleep(1)

# Handling Alert by clicking on "Cancel" button using dismiss() method
alert_input.send_keys(name)
alert_input.find_element(By.XPATH, confirm_alert_btn).click()
confirm_alert_wind = driver.switch_to.alert
assert confirm_alert_wind.text == confirm_alert_txt
sleep(1)
confirm_alert_wind.dismiss()

sleep(2)
driver.quit()
