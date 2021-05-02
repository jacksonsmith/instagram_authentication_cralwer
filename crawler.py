from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

getdriver = ("https://www.instagram.com/")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(getdriver)

time.sleep(3)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)

time.sleep(3)

driver.find_element_by_xpath("//div[text()='Log In']").click()

time.sleep(3)

driver.find_element_by_xpath("//button[text()='Not Now']").click()

time.sleep(3)

driver.find_element_by_xpath("//button[text()='Not Now']").click()