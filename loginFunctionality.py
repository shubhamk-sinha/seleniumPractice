from driverInitialization import Driverinitialization as DI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

loginpage_url = "https://rahulshettyacademy.com/loginpagePractise/"
pageTitle = "LoginPage Practise | Rahul Shetty Academy"
childpageTitle = "RS Academy"
blinkingTextxpath = '//a[@class="blinkingText"]'
childpageTextxpath = '//p[@class="im-para red"]'
usernameInputid = "username"
passwordInputid = "password"
userTypedropdownxpath = '//select[@class="form-control"]'
agreementCheckboxcss = 'input[type="checkbox"]'
invalidLoginerrormsgxpath = '//div[contains(@class,"alert-danger")]'
error_msg = "Incorrect username/password."

driver = DI.chrome_driver
wait = WebDriverWait(driver, 10)
driver.get(loginpage_url)
assert driver.title == pageTitle
floating_link = driver.find_element(By.XPATH, blinkingTextxpath)
wait.until(ec.presence_of_element_located((By.XPATH, blinkingTextxpath)))

floating_link.click()
windows_tab = driver.window_handles
driver.switch_to.window(windows_tab[1])
assert driver.title == childpageTitle
childpageText = driver.find_element(By.XPATH, childpageTextxpath).text
emailExtracted = childpageText.split(" ")
driver.close()

driver.switch_to.window(windows_tab[0])
driver.find_element(By.ID, usernameInputid).send_keys(emailExtracted[4])
driver.find_element(By.ID, passwordInputid).send_keys("learning")
userType_dropdown = Select(driver.find_element(By.XPATH, userTypedropdownxpath))
userType_dropdown.select_by_value("teach")  # selecting user as a Teacher
dp_txt = driver.find_element(By.XPATH, userTypedropdownxpath).get_attribute("value")
TandCcheckbox = driver.find_element(By.CSS_SELECTOR, agreementCheckboxcss)
TandCcheckbox.click()
assert dp_txt == "teach"
assert TandCcheckbox.is_selected()
driver.find_element(By.NAME, "signin").click()

wait.until(ec.visibility_of_element_located((By.XPATH, invalidLoginerrormsgxpath)))
error_login_text = driver.find_element(By.XPATH, invalidLoginerrormsgxpath).text
assert error_login_text == error_msg

driver.quit()
