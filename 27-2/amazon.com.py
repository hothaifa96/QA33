from selenium import webdriver # chromedriver
from selenium.webdriver.common.by import By # using method
from selenium.webdriver.common.keys import Keys # keys on the keyboard
import time

driver = webdriver.Chrome();
driver.get('https://www.ebay.com/')
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR , '#gh-ac')
search.send_keys('coffee machine')
time.sleep(1)
search_btn= driver.find_element(By.CSS_SELECTOR, '#gh-btn')
search_btn.click()
time.sleep(1)
price = driver.find_element(By.CSS_SELECTOR ,'#srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span')
price =round(float(price.text[3:]))
print(price)
# item1 = driver.find_element(By.CSS_SELECTOR, '#srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > a')
# item1.click()
print(driver.title)


