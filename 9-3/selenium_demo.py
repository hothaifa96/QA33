from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def open_site(driver, url):
    driver.get(url)
    time.sleep(3)
    return driver.current_url


def login(driver, username, password1):
    name = driver.find_element(By.CSS_SELECTOR, '#username')
    name.send_keys(username)
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys(password1)
    button = driver.find_element(By.CSS_SELECTOR, '#log-in')
    button.click()
    time.sleep(3)
    return driver.current_url


def get_balance(driver):
    balance = driver.find_element(By.CSS_SELECTOR,'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)')
    balance = float(balance.text[1:])
    return balance
