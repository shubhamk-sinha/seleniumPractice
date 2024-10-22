from selenium.webdriver.common.by import By
from pageObjects.greenKartCountrypage import GKCountrypage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class GKCheckout:

    promo_code_input = (By.XPATH, '//input[@class="promoCode"]')
    promo_apply_btn = (By.XPATH, '//button[@class="promoBtn"]')
    promo_info = (By.XPATH, '//span[@class="promoInfo"]')
    cart_table_rows = (By.XPATH, '//table[@id="productCartTables"]/tbody/tr')
    discount_applied_val = (By.XPATH, '//span[@class="discountPerc"]')
    cart_table_total_column_val = (By.XPATH, '//b[text()="Total"]/parent::td//following::tr/td[5]/p[@class="amount"]')
    total_item_value_ui_label = (By.XPATH, '//span[@class="totAmt"]')
    after_dis_val_ui = (By.XPATH, '//span[@class="discountAmt"]')
    place_order_btn = (By.XPATH, '//button[text()="Place Order"]')
    promoinfo_xpath = (By.XPATH, '//span[@class="promoInfo"]')
    cart_table_rows = (By.XPATH, '//table[@id="productCartTables"]/tbody/tr')

    def __init__(self, driver):
        self.driver = driver

    def applyPromocode(self, code_text):
        self.driver.find_element(*GKCheckout.promo_code_input).send_keys(code_text)
        self.driver.find_element(*GKCheckout.promo_apply_btn).click()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((GKCheckout.promoinfo_xpath)))
        return len(self.driver.find_elements(*GKCheckout.cart_table_rows))

        
    def getDiscountValue(self):
        return self.driver.find_element(*GKCheckout.discount_applied_val).text
    
    def getTotalval(self):
        return self.driver.find_elements(*GKCheckout.cart_table_total_column_val)
    
    def getTotalfromUI(self):
        return int(self.driver.find_element(*GKCheckout.total_item_value_ui_label).text)
    
    def getTotalafterDiscount(self):
        return float(self.driver.find_element(*GKCheckout.after_dis_val_ui).text)
    
    def placeOrder(self):
        self.driver.find_element(*GKCheckout.place_order_btn).click()
        return GKCountrypage(self.driver)