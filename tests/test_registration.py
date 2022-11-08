from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from conftest import login_url


class TestRegistration:
    def test_registration_success(self, random_email, random_password, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.reg_link).click()
        driver.find_element(By.XPATH, locators.reg_name_input).send_keys('Василий')
        driver.find_element(By.XPATH, locators.reg_email_input).send_keys(random_email)
        driver.find_element(By.XPATH, locators.reg_password_input).send_keys(random_password)
        driver.find_element(By.XPATH, locators.reg_submit_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url

    def test_registration_password_error(self, random_email, driver):
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        driver.find_element(By.LINK_TEXT, locators.reg_link).click()
        driver.find_element(By.XPATH, locators.reg_name_input).send_keys('Алексей')
        driver.find_element(By.XPATH, locators.reg_email_input).send_keys(random_email)
        driver.find_element(By.XPATH, locators.reg_password_input).send_keys('123')
        driver.find_element(By.XPATH, locators.reg_submit_button).click()
        assert driver.find_element(By.CLASS_NAME, locators.reg_password_error).text == 'Некорректный пароль'
