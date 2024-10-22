from selenium.webdriver.common.by import By


class GKOrderPlacedPage:

    success_order_txt_xpath = (By.XPATH, '//div[@class="wrapperTwo"]/span')

    def __init__(self, driver):
        self.driver = driver

    def getOrderconfirmation(self):
        return self.driver.find_element(*GKOrderPlacedPage.success_order_txt_xpath).text