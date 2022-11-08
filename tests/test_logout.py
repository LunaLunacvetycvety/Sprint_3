from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from conftest import login_url


class TestLogout:
    def test_logout_success(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys('Alexey@mail.ru')
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys('Lesha56142')
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.log_out)))
        driver.find_element(By.XPATH, locators.log_out).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
