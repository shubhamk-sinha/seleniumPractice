from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class GKHomepage():
    search_input = (By.XPATH, '//input[@class="search-keyword"]')
    product_results = (By.XPATH, '//div[@class="product"]')
    
    def __init__(self, driver):
        self.driver = driver

    def hompageSearch(self, search_text):
        return self.driver.find_element(*GKHomepage.search_input).send_keys(search_text)    
    
    def getProducts(self):
        return self.driver.find_elements(*GKHomepage.product_results)
    
    def isRedirected(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((GKHomepage.search_input)))
        if self.driver.find_element(*GKHomepage.search_input):
            return True
        else:
            return False
