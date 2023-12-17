#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
import time

#if you want to leave the window open for inspection:
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

driver.get("http://www.weather.gov")
elem = driver.find_element(By.NAME, "inputstring")
elem.click()
elem.send_keys("19038")
time.sleep(1)
elem.send_keys(Keys.RETURN)
time.sleep(1)
findforecast = driver.find_element(By.CLASS_NAME,"myforecast-current")
findtmp = driver.find_element(By.CLASS_NAME,"myforecast-current-lrg")
temp = findtmp.get_attribute("innerHTML")
conditions = findforecast.get_attribute("innerHTML")

print(f"Conditions: {conditions}")
print(f"Temperature: {temp}")
