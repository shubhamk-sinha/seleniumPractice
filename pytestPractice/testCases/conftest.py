import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Input browser name. 'chrome' for Chrome browser,\
                  'geeko' for firefox, 'IE' for internet explorer.\
                    default is chrome.",
    )


@pytest.fixture(scope="class")
def openBrowser(request):
    browser_name = request.config.getoption("browser")
    match browser_name:
        case "chrome":
            maximize = "--start-maximized"
            chrome_properties = Options()
            chrome_properties.add_argument(maximize)
            chrome_properties.add_experimental_option(
                "excludeSwitches", ["enable-automation"]
            )  # disables infobar
            driver = webdriver.Chrome(options=chrome_properties)

        case "geeko":
            driver = webdriver.Firefox()

        case _:
            driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()
