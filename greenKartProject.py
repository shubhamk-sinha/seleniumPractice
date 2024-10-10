from driverInitialization import Driverinitialization as DI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep

total_value_of_items = 0
greenkart_url = 'https://rahulshettyacademy.com/seleniumPractise/#/'
page_title = 'GreenKart - veg and fruits kart'
search_text = 'ca'
search_input = '//input[@class="search-keyword"]'
product_results = '//div[@class="product"]'
add_to_cart_btn = '//button[text()="ADD TO CART"]'
open_cart_btn = '//img[@alt="Cart"]'
proceed_to_checkout_btn = '//button[text()="PROCEED TO CHECKOUT"]'
place_order_btn = '//button[text()="Place Order"]'
promo_code_input = '//input[@class="promoCode"]'
promo_code_text = 'rahulshettyacademy'
promo_apply_btn = '//button[@class="promoBtn"]'
cart_table_rows = '//table[@id="productCartTables"]/tbody/tr'
cart_table_total_column_val = '//b[text()="Total"]/parent::td//following::tr/td[5]/p[@class="amount"]'
total_item_value_ui_label = '//span[@class="totAmt"]'
discount_applied_val = '//span[@class="discountPerc"]'
after_dis_val_ui = '//span[@class="discountAmt"]'
choose_country_label = '//label[text()="Choose Country"]'
country_dropdown_xpath = '//select'
country_name = 'India'
tandc_checkbox = '//input[@class="chkAgree"]'
country_proceed_btn = '//button[text()="Proceed"]'
success_order_txt_xpath = '//div[@class="wrapperTwo"]/span'
success_message = f"Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"

driver = DI.chrome_driver
driver.get(greenkart_url)
assert driver.title == page_title

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, search_input).send_keys(search_text)
sleep(2)
products = driver.find_elements(By.XPATH, product_results)
assert len(products) == 4
for product in products:
    product.find_element(By.XPATH, add_to_cart_btn).click()

driver.find_element(By.XPATH, open_cart_btn).click()
driver.find_element(By.XPATH, proceed_to_checkout_btn).click()

#checkout page
driver.find_element(By.XPATH, promo_code_input).send_keys(promo_code_text)
driver.find_element(By.XPATH, promo_apply_btn).click()
wait.until(ec.presence_of_element_located((By.XPATH, '//span[@class="promoInfo"]')))
assert len(driver.find_elements(By.XPATH, cart_table_rows)) == len(products)
dis_val = driver.find_element(By.XPATH, discount_applied_val).text
assert dis_val == '10%'
for value in driver.find_elements(By.XPATH, cart_table_total_column_val):
    total_val = value.text
    total_value_of_items += int(total_val)

assert total_value_of_items == int(driver.find_element(By.XPATH, total_item_value_ui_label).text)
total_after_dis_val_ui = float(driver.find_element(By.XPATH, after_dis_val_ui).text)
assert float(total_value_of_items - (total_value_of_items*0.1)) == float(total_after_dis_val_ui)
driver.find_element(By.XPATH, place_order_btn).click()

#country page
wait.until(ec.presence_of_element_located((By.XPATH, choose_country_label)))
country_dropdown = Select(driver.find_element(By.XPATH, country_dropdown_xpath))
country_dropdown.select_by_value(country_name)
assert driver.find_element(By.XPATH, country_dropdown_xpath).get_attribute("value") == country_name
checkbox_term_cond = driver.find_element(By.XPATH, tandc_checkbox)
checkbox_term_cond.click()
assert checkbox_term_cond.is_selected()
driver.find_element(By.XPATH, country_proceed_btn).click()

#Order Placed Successfully Page
success_text_ui = driver.find_element(By.XPATH, success_order_txt_xpath).text
assert success_text_ui == success_message

#Redirect to homepage
wait.until(ec.presence_of_element_located((By.XPATH, search_input)))
assert driver.current_url == greenkart_url

sleep(3)
driver.quit()