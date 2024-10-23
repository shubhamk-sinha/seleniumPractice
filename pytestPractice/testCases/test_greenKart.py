from utilities.baseClass import BaseClass
from pageObjects.greenKartHomepage import GKHomepage
from pageObjects.greenKartCartpage import GKCartpage
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import softest

class TestOne(BaseClass, softest.TestCase):

    def test_greenKartcheckout(self):
        total_value_of_items = 0
        greenkart_url = 'https://rahulshettyacademy.com/seleniumPractise/#/'
        page_title = 'GreenKart - veg and fruits kart'
        search_text = 'ca'
        # search_input = '//input[@class="search-keyword"]'
        promo_code_text = 'rahulshettyacademy'
        country_name = 'India'
        success_message = f"Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"

        self.driver.get(greenkart_url)
        # assert self.driver.title == page_title
        self.soft_assert(self.assertEqual, self.driver.title, page_title, msg="Title Mismatch.")

        homePage = GKHomepage(self.driver)
        homePage.hompageSearch(search_text)    
        sleep(1)
        products = homePage.getProducts()
        # assert len(products) == 4
        self.soft_assert(self.assertEqual, len(products), 4, msg="Product Count Mismatch.")

        cartPage = GKCartpage(self.driver)
        for product in products:
            cartPage.addToCart(product).click()
        cartPage.openCart().click()
        checkoutPage = cartPage.proceedTocheckout()

        #checkout page
        cart_items = checkoutPage.applyPromocode(promo_code_text)
        # assert cart_items == len(products)
        self.soft_assert(self.assertEqual, cart_items, len(products), msg="Product Count Mismatch on Checkout Page.")


        dis_val = checkoutPage.getDiscountValue()
        # assert dis_val == '10%'
        self.soft_assert(self.assertEqual, dis_val, '10%', msg="Discount applied is not 10%.")
        for value in checkoutPage.getTotalval():
            total_val = value.text
            total_value_of_items += int(total_val)

        # assert total_value_of_items == checkoutPage.getTotalfromUI()
        self.soft_assert(self.assertEqual, total_value_of_items, checkoutPage.getTotalfromUI(), msg="Total value do not match!")
        total_after_discount = checkoutPage.getTotalafterDiscount()
        # assert float(total_value_of_items - (total_value_of_items*0.1)) == total_after_discount
        self.soft_assert(self.assertEqual, float(total_value_of_items - (total_value_of_items*0.1)), total_after_discount, msg="Total after discount not equal.")

        countryPage = checkoutPage.placeOrder()

        #country page
        selected_country = countryPage.selectCountry(country_name)
        # assert selected_country == country_name
        self.soft_assert(self.assertEqual, selected_country, country_name, msg=f"Selected Country is not {country_name}!")
        checkbox_term_cond = countryPage.selectTermandCondition()
        checkbox_term_cond.click()
        # assert checkbox_term_cond.is_selected()
        self.soft_assert(self.assertTrue, checkbox_term_cond.is_selected(), msg="Term and Condition not Selected!")
        placeOrderPage = countryPage.placeOrder()

        #Order Placed Successfully Page
        success_text_ui = placeOrderPage.getOrderconfirmation()
        assert success_text_ui == success_message

        #Redirect to homepage
        # assert homePage.isRedirected()
        self.soft_assert(self.assertTrue, homePage.isRedirected(), msg="Redirect to Homepage Failed!")
        sleep(2)
        self.assert_all()