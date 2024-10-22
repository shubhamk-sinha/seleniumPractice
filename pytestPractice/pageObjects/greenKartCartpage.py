from selenium.webdriver.common.by import By
from pageObjects.greenKartCheckoutpage import GKCheckout

class GKCartpage:

    add_to_cart_btn = (By.XPATH, '//button[text()="ADD TO CART"]')
    open_cart_btn = (By.XPATH, '//img[@alt="Cart"]')
    proceed_to_checkout_btn = (By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self, product):
        return product.find_element(*GKCartpage.add_to_cart_btn)

    def openCart(self):
        return self.driver.find_element(*GKCartpage.open_cart_btn)
    
    def proceedTocheckout(self):
        self.driver.find_element(*GKCartpage.proceed_to_checkout_btn).click()
        return GKCheckout(self.driver)
        