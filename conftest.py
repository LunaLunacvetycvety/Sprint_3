import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def driver():
    browser_driver = webdriver.Chrome()
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()


@pytest.fixture
def random_password(request):
    symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(request.param):
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


@pytest.fixture
def registered_user(random_email, random_password, driver):
    driver.find_element(By.LINK_TEXT, locators.account_button).click()
    driver.find_element(By.LINK_TEXT, locators.reg_link).click()
    driver.find_element(By.XPATH, locators.reg_name_input).send_keys('Василий')
    driver.find_element(By.XPATH, locators.reg_email_input).send_keys(random_email)
    driver.find_element(By.XPATH, locators.reg_password_input).send_keys(random_password)
    driver.find_element(By.XPATH, locators.reg_submit_button).click()
    return {'email': random_email, 'password': random_password}

