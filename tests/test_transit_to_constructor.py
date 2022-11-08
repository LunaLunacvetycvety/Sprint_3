from selenium.webdriver.common.by import By
import locators
from conftest import url


class TestTransitToConstructor:
    def test_transit_to_constructor_from_button_success(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys('Alexey@mail.ru')
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys('Lesha56142')
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.constructor_button).click()
        assert driver.current_url == url

    def test_transit_to_constructor_from_logo_success(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys('Alexey@mail.ru')
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys('Lesha56142')
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.XPATH, locators.logo_link).click()
        assert driver.current_url == url
