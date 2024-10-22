from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from pageObjects.greenKartOrderPlacedPage import GKOrderPlacedPage

class GKCountrypage:

    choose_country_label = (By.XPATH, '//label[text()="Choose Country"]')
    country_dropdown_xpath = (By.XPATH, '//select')
    tandc_checkbox = (By.XPATH, '//input[@class="chkAgree"]')
    country_proceed_btn = (By.XPATH, '//button[text()="Proceed"]')

    def __init__(self, driver):
        self.driver = driver

    def selectCountry(self, country_name):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((GKCountrypage.choose_country_label)))
        country_dropdown = Select(self.driver.find_element(*GKCountrypage.country_dropdown_xpath))
        country_dropdown.select_by_value(country_name)
        return self.driver.find_element(*GKCountrypage.country_dropdown_xpath).get_attribute("value")
    
    def selectTermandCondition(self):
        return self.driver.find_element(*GKCountrypage.tandc_checkbox)
    
    def placeOrder(self):
        self.driver.find_element(*GKCountrypage.country_proceed_btn).click()
        return GKOrderPlacedPage(self.driver)
