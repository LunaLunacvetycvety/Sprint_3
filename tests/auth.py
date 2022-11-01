import time
from selenium.webdriver.common.by import By
import locators
from conftest import url
import pytest


class TestAuth:
    @pytest.mark.parametrize('random_password', [8], indirect=True)
    def test_auth_main_screen_success(self, registered_user, driver, random_password):
        time.sleep(1)
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys(registered_user.get('email'))
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys(registered_user.get('password'))
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        time.sleep(1)
        assert driver.current_url == url

    def test_main_auth_from_account_success(self, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        assert driver.current_url == url + 'login'

    def test_main_auth_success(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        assert driver.current_url == url + 'login'

    def test_auth_from_reg_success(self, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.reg_link).click()
        driver.find_element(By.LINK_TEXT, locators.sign_in_button).click()
        assert driver.current_url == url + 'login'

    def test_auth_from_recovery_password_success(self, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.recovery_password).click()
        driver.find_element(By.LINK_TEXT, locators.sign_in_button).click()
        assert driver.current_url == url + 'login'
