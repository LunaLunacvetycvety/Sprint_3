import time
from selenium.webdriver.common.by import By
import locators
from conftest import url
import pytest


class TestLogout:
    @pytest.mark.parametrize('random_password', [8], indirect=True)
    def test_logout_success(self, registered_user, driver, random_password):
        time.sleep(1)
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys(registered_user.get('email'))
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys(registered_user.get('password'))
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.log_out).click()
        time.sleep(1)
        assert driver.current_url == url + 'login'
