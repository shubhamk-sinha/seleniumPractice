from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driverinitialization:
    maximize = "--start-maximized"

    chrome_properties = Options()
    chrome_properties.add_argument(maximize)
    chrome_properties.add_experimental_option("excludeSwitches", ["enable-automation"]) #disables infobar

    chrome_driver = webdriver.Chrome(options=chrome_properties)
    chrome_driver.implicitly_wait(5)