import random
import time
import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site/'
login_url = url + 'login'

@pytest.fixture
def driver():
    browser_driver = webdriver.Chrome()
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()


@pytest.fixture
def random_password():
    symbols = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(8):
        password += random.choice(symbols)
    return password


@pytest.fixture
def random_email():
    length = 3
    letters = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    email = ''
    time_stamp = time.time()
    for i in range(length):
        email += random.choice(letters)
    return email + str(time_stamp) + "@gmail.com"

