from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from conftest import url


class TestTransitToAccount:
    def test_auth_main_screen_success(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        driver.find_element(By.XPATH, locators.auth_email_input).send_keys('Alexey@mail.ru')
        driver.find_element(By.XPATH, locators.auth_password_input).send_keys('Lesha56142')
        driver.find_element(By.XPATH, locators.auth_submit_button).click()
        driver.find_element(By.LINK_TEXT, locators.account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(url + 'account/profile'))
        assert driver.current_url == url + 'account/profile'
