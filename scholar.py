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

driver.get("http://scholar.google.com")
elem = driver.find_element(By.NAME, "q")
elem.click()
elem.send_keys("sonic hedgehog")
time.sleep(1)
elem.send_keys(Keys.RETURN)
time.sleep(1)


external_link_xpath = "//a[starts-with(@href,'https') and not(contains(@href, 'google'))]"

first_link = driver.find_element(By.XPATH,external_link_xpath)
cnt = first_link.get_attribute("innerHTML")


links = driver.find_elements(By.XPATH,external_link_xpath)

articles = []
for link in links:
    href = link.get_attribute("href")
    content = link.get_attribute("innerHTML")
    articles.append( (content, href) )

#first_link.click()
print(articles)


