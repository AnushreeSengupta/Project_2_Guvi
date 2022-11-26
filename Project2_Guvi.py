
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#Test Objective -Successful Employee login to OrangeHRM portal

def TC_Login_01(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)
    driver.close()


TC_Login_01("firefox")
print("User login is successful!")

#Test Objective -Invalid Employee login to OrangeHRM portal

def TC_Login_02(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    actionchains =ActionChains(driver)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("Invalid Password")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)
    ele=driver.find_element(By.XPATH, value='//p[text()="Invalid credentials"]')
    if ele.text == "Invalid credentials":
        print("Test Case passed")
    else:
        print("Test Case failed")
    driver.close()


TC_Login_02("firefox")

time.sleep(5)

#TC_PIM_01 - Add a new employee in the PIM module
#TC_PIM_02 - Edit an exiting employee in the PIM module.
#TC_PIM_03 - Test Objective -Delete an existing employee from portal


def TC_PIM_01_02_03(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    actionChains =ActionChains(driver)



    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)


#Add an employee
    driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]').click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(1)").click()
    time.sleep(10)
    driver.find_element(By.XPATH, value='//input[@placeholder="First Name"]').send_keys("Amaila")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//input[@placeholder="Middle Name"]').send_keys("Marry")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//input[@placeholder="Last Name"]').send_keys("Peter")
    time.sleep(5)
    #delete employee id
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-grid-2:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-grid-2:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("1236")
    #Create Login Details
    driver.find_element(By.CSS_SELECTOR, value=".oxd-switch-input").click()
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("AmailaMarry")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, value=".user-password-cell > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Amaila01234@pw")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Amaila01234@pw")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//button[@type="submit"]').click()
    time.sleep(10)


    #Employee Personal Details Open

    #driver.find_element(By.CSS_SELECTOR, value="div.orangehrm-horizontal-padding:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Nupur")
    time.sleep(2)
    #license
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input").send_keys("MP201234789")
    time.sleep(5)
    # Save
    #driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(2)").click()
    #driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']']").click()
    time.sleep(10)

#Go to Contact Details add details
    driver.find_element(By.XPATH,'//a[text()="Contact Details"]').click()
    time.sleep(5)
    #City
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys("NewYork")
    #Mobile
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys("9911991192")
    time.sleep(5)
    #EMAIL ID
    driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input').send_keys("admaila@gmail.com")
    #Save
    driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(2)").click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    #Job Details

    driver.find_element(By.XPATH, '//a[text()="Job"]').click()
    time.sleep(10)
    #driver.find_element(By.XPATH,'//span[text()="Account Assistant"]').click()
    #driver.find_element(By.XPATH,'//div[text()="Account Assistant"]').click()
    #driver.find_element(By.XPATH,'//*[text()="Chief Executive Officer"]').click()
    #time.sleep(5)
    #driver.find_element(By.XPATH, '//span[text()="Official and Managers"]').click()
    #time.sleep(5)
    #driver.find_element(By.XPATH, '//span[text()="Full-Time Contract"]').click()
    time.sleep(5)
    #driver.find_element(By.XPATH,'//button[@type="submit"]').click()


#Deleting an existing employee
    time.sleep(5)
    driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]').click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//div[@class='orangehrm-container']//div[3]//div[1]//div[9]//div[1]//button[1]//i[1]").click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()
    time.sleep(5)
    driver.close()
TC_PIM_01_02_03("firefox")