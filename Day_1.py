# importing required modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

# Automation code below
chrome_driver_path = Service(r"C:/Users/kumar_shu/Downloads/chromedriver.exe") #using service class for defining driver path

# using options class to set chrome properties
chrome_properties = Options()
chrome_properties.add_argument("--start-maximized")
chrome_properties.add_experimental_option("excludeSwitches", ["enable-automation"]) #disables infobar

#initializing driver
driver = webdriver.Chrome(options= chrome_properties, service=chrome_driver_path)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#validating page title
assert "Practice Page" in driver.title

sleep(3)
driver.quit()