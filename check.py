from driverInitialization import Driverinitialization as DI
from selenium.webdriver.common.by import By
from time import sleep

driver = DI.chrome_driver
driver.get("https://tus.io/demo")

sleep(1)

driver.execute_script('document.getElementById("P0-0").scrollIntoView();')
driver.execute_script('document.getElementById("P0-0").scrollIntoView();')
driver.execute_script('document.getElementById("P0-0").scrollIntoView();')

sleep(0.5)
driver.find_element(By.XPATH, '//input[@id="P0-0"]').send_keys(r"C:\Users\kumar_shu\Downloads\testFile.txt")

sleep(5)

driver.quit()