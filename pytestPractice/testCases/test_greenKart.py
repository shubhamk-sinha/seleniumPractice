from utilities.baseClass import BaseClass
from pageObjects.greenKartHomepage import GKHomepage
from pageObjects.greenKartCartpage import GKCartpage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class TestOne(BaseClass):

    def test_greenKartcheckout(self):
        total_value_of_items = 0
        greenkart_url = 'https://rahulshettyacademy.com/seleniumPractise/#/'
        page_title = 'GreenKart - veg and fruits kart'
        search_text = 'ca'
        search_input = '//input[@class="search-keyword"]'
        promo_code_text = 'rahulshettyacademy'
        country_name = 'India'
        success_message = f"Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"

        self.driver.get(greenkart_url)
        assert self.driver.title == page_title

        wait = WebDriverWait(self.driver, 10)
        homePage = GKHomepage(self.driver)
        homePage.hompageSearch(search_text)    
        sleep(1)
        products = homePage.getProducts()
        assert len(products) == 4
        cartPage = GKCartpage(self.driver)
        for product in products:
            cartPage.addToCart(product).click()
        cartPage.openCart().click()
        checkoutPage = cartPage.proceedTocheckout()

        #checkout page
        cart_items = checkoutPage.applyPromocode(promo_code_text)
        assert cart_items == len(products)

        dis_val = checkoutPage.getDiscountValue()
        assert dis_val == '10%'
        for value in checkoutPage.getTotalval():
            total_val = value.text
            total_value_of_items += int(total_val)

        assert total_value_of_items == checkoutPage.getTotalfromUI()
        total_after_discount = checkoutPage.getTotalafterDiscount()
        assert float(total_value_of_items - (total_value_of_items*0.1)) == total_after_discount
        countryPage = checkoutPage.placeOrder()

        #country page
        selected_country = countryPage.selectCountry(country_name)
        assert selected_country == country_name
        checkbox_term_cond = countryPage.selectTermandCondition()
        checkbox_term_cond.click()
        assert checkbox_term_cond.is_selected()
        placeOrderPage = countryPage.placeOrder()

        #Order Placed Successfully Page
        success_text_ui = placeOrderPage.getOrderconfirmation()
        assert success_text_ui == success_message

        #Redirect to homepage
        is_redirected = homePage.isRedirected()
        print(f'is_redirected value: {is_redirected}, type: {type(is_redirected)}')
        assert is_redirected

        sleep(2)