import pytest

from selenium_demo import *
from selenium import webdriver


class TestBank:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    @pytest.fixture
    def url(self):
        return 'https://demo.applitools.com/'

    def test_sanity(self,driver,url):
        expected = url
        actual = open_site(driver, expected)
        assert expected == actual

    @pytest.mark.parametrize('username, password',[ ('hodi','123'),('miriam','miri1234') ])
    def test_login_p(self,driver,url,username,password):
        expected = 'https://demo.applitools.com/app.html'
        open_site(driver, url)
        actual = login(driver, username, password)
        assert actual == expected

    def test_balance_under_1000(self,driver,url):
        expected = 1000
        open_site(driver,url)
        login(driver,'hodi','123')
        actual= get_balance(driver)
        assert actual < expected