from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('/Users/hothaifa/Desktop/chromedriver')
url= 'https:/demo.applitools.com/'
username_selector = '#username'
password_selector = '#password'
login_selector = '#log-in'
credit_selector = 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(2) > div.balance-value'
balance_selector = 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)'

# --------- enter the url --------
driver.get(url)
# --------- enter the url --------

time.sleep(2)

# ---------login --------
username_textbox =driver.find_element(By.CSS_SELECTOR,username_selector)
username_textbox.send_keys('admin')
driver.find_element(By.CSS_SELECTOR,password_selector).send_keys('password')
driver.find_element(By.CSS_SELECTOR,login_selector).click()
#--------login ----------

time.sleep(2)

# --------- data collector ------------
balance = driver.find_element(By.CSS_SELECTOR ,balance_selector).text
credit = driver.find_element(By.CSS_SELECTOR ,credit_selector).text
# --------- data collector ------------

time.sleep(2)

balance = float(balance[1:])
credit= float(credit[1:].replace(',',''))

print(f'total balance -> {balance+credit} ')




