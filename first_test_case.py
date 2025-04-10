# Test Case(Steps to automate) :->

# 1) Open Chrome
# 2) open the url : https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3) provide email
# 4) provide password
# 5) Click on Login   
# 6) Capture the title of the Dasboard page 
# 7) Verify the title of the page ( should be "Dasboard / "nopCommerece Administration)
# 8) Close browser

# 9) If the Verification pass -> success , else Fail

# -----------------------------------------------------------------------------------------------------------------------

# NOte : Web driver is a module which is avaialbble in the selenium package 
# we need to import it.

# ---------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
chrome_driver_path = '/home/shtlp_0059/Drivers/chromedriver-linux64/chromedriver'

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Create a WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
# This will automatically launch the browser

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

time.sleep(2)  # Small wait to let elements load

# now we need to identify the web element ie. input/textarea for the useranme and password
driver.find_element(By.NAME, 'username').send_keys("Admin")
driver.find_element(By.NAME, 'password').send_keys("admin123")
driver.find_element(By.CLASS_NAME, 'orangehrm-login-button').click()

# Now check the title of the page ( to confirm we logged into the correct page !! )

act_title = driver.title              # it will give us the title of webpage(Dashboard) 
expected_title = "OrangeHRM"

# now compare the title
if act_title == expected_title:
    print('login test passes')
else:
    print('login test failed')
