from selenium.webdriver.common.by import By
import locators
import time
import pytest
from conftest import url


class TestRegistration:
    @pytest.mark.parametrize('random_password', [8], indirect=True)
    def test_registration_success(self, random_email, random_password, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.reg_link).click()
        driver.find_element(By.XPATH, locators.reg_name_input).send_keys('Василий')
        driver.find_element(By.XPATH, locators.reg_email_input).send_keys(random_email)
        driver.find_element(By.XPATH, locators.reg_password_input).send_keys(random_password)
        driver.find_element(By.XPATH, locators.reg_submit_button).click()
        time.sleep(1)
        assert driver.current_url == url + 'login'

    @pytest.mark.parametrize('random_password', [3], indirect=True)
    def test_registration_password_error(self, random_email, random_password, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.reg_link).click()
        driver.find_element(By.XPATH, locators.reg_name_input).send_keys('Алексей')
        driver.find_element(By.XPATH, locators.reg_email_input).send_keys(random_email)
        driver.find_element(By.XPATH, locators.reg_password_input).send_keys(random_password)
        driver.find_element(By.XPATH, locators.reg_submit_button).click()
        assert driver.find_element(By.CLASS_NAME, locators.reg_password_error).text == 'Некорректный пароль'
