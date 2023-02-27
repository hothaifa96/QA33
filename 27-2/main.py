from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get('https://google.com')
driver.maximize_window()
# print(driver.current_url)
# time.sleep(1)
# driver.get('https://ebay.com')
# driver.back()
# time.sleep(1)
# driver.forward()
# driver.refresh()
# time.sleep(1)
#
# title = driver.title # the title of any website
# print(title)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('mama maglione Pizza')
search_box.send_keys( Keys.ENTER )
time.sleep(3)

link = driver.find_element(By.CSS_SELECTOR,'#gh-logo')
link.click()

time.sleep(5)



