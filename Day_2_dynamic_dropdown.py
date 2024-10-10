from driverInitialization import Driverinitialization as DI
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Defining variables section
maximize = "--start-maximized"
webpage_url = "https://rahulshettyacademy.com/dropdownsPractise/"
page_title = (
    "QAClickJet - Flight Booking for Domestic and International, Cheap Air Tickets"
)
country_searchbox = '//input[@placeholder="Type to Select"]'
search_country = "India"
searched_country_xpath = '//a[text()="India"]'

driver = DI.chrome_driver

driver.get(webpage_url)
assert page_title in driver.title

driver.find_element(By.XPATH, country_searchbox).send_keys(search_country)

wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.XPATH, searched_country_xpath)))

dynamic_dropdown = driver.find_element(By.XPATH, searched_country_xpath)
dynamic_dropdown.click()

# To get value from a dynamic text use get_attribute("value") method.
selected_country = driver.find_element(By.XPATH, country_searchbox).get_attribute("value")
assert selected_country == search_country

sleep(5)
driver.quit()