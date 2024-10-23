import driverInitialization as DI
from time import sleep
from selenium.webdriver.common.by import By

def singleFile():
    print(f"Started Executing Single File Upload......\n\n")
    driver = DI.Driverinitialization.chrome_driver
    driver.get("https://practice.expandtesting.com/upload")
    sleep(2)
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys("C:\\Users\\kumar_shu\\Downloads\\testFile.txt")
    sleep(2)
    driver.execute_script('document.getElementById("fileSubmit").scrollIntoView();')
    driver.find_element(By.XPATH, '//button[@id="fileSubmit"]').click()
    check_upload = driver.find_element(By.XPATH, '//h1[text()="File Uploaded!"]').text
    filename = driver.find_element(By.XPATH, '//div[@id="uploaded-files"]/p').text
    formatted_fn = filename.split("_")
    print(formatted_fn[1])
    sleep(2)
    print(f"Successfuly Executed Single File Upload......\n\n")


def multipleFile():
    print(f"Started Executing Multiple File Upload......\n\n")
    tf1 = "C:\\Users\\kumar_shu\\Downloads\\testData.pdf"
    tf2 = "C:\\Users\\kumar_shu\\Downloads\\testData(2).pdf"
    driver = DI.Driverinitialization.chrome_driver
    sleep(2)
    driver.get("https://www.patternfly.org/components/file-upload/multiple-file-upload/")
    driver.execute_script('document.getElementById("ws-react-c-multiple-file-upload-basic").scrollIntoView();')
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(tf1)
    sleep(0.5)
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(tf2)
    sleep(3)
    driver.quit()
    print(f"Successfuly Executed Multiple File Upload......\n\n")


if __name__ == "__main__":
    # singleFile()
    multipleFile()