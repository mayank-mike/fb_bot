from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

user_email=sys.argv[1]
user_password=sys.argv[2]

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("https://www.facebook.com/login/")

email=driver.find_element_by_id("email")
password=driver.find_element_by_id("pass")

email.clear()
password.clear()
email.send_keys(user_email)
time.sleep(2)
password.send_keys(user_password)
time.sleep(1)

driver.find_element_by_id("loginbutton").click()

time.sleep(1000)
driver.close()
