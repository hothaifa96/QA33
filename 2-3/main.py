from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/hothaifa/Desktop/chromedriver')  # windows add .exe
url = 'https://demo.applitools.com/'
starbucks_selector ='body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td.text-right.bolder.nowrap > span'
stripe_selector ='body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td.text-right.bolder.nowrap > span'


def get_number(text):
    amount = text[2:-4]  # 1,250
    f = float(amount.replace(',', ''))
    return f


def select(selector, driver):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return element


def login(username, passwrd, driver):
    username_text = select('#username', driver)
    username_text.send_keys(username)

    password = select('#password', driver)
    password.send_keys(passwrd)

    signup = driver.find_element(By.CSS_SELECTOR, '#log-in')
    signup.click()

    time.sleep(3)


# driver.get('https://www.google.com') # opens a given url
# time.sleep(2)
#
# element_textbox = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
# time.sleep(2)
#
# element_textbox.send_keys('mama maglione')
# time.sleep(2)
# element_textbox.send_keys(Keys.ENTER)
# time.sleep(2)
# step 1 open the site
driver.get(url)
time.sleep(3)
# step 2 login
login('hodi123', '1234', driver)  # this function log in
# get the starbucks amount
starbucks = select(starbucks_selector,driver)
starbucks_amount = get_number(starbucks.text)
stripe = select(stripe_selector,driver)
stripe_amount = get_number(stripe.text)
print(max(stripe_amount, starbucks_amount))
driver.close()
