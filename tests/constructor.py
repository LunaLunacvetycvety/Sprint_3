from selenium.webdriver.common.by import By
import locators


class TestConstructor:
    def test_transit_to_bread_success(self, driver):
        driver.find_element(By.XPATH, locators.sauces_button).click()
        driver.find_element(By.XPATH, locators.bread_button).click()

    def test_transit_to_sauces_success(self, driver):
        driver.find_element(By.XPATH, locators.sauces_button).click()

    def test_transit_to_filling_success(self, driver):
        driver.find_element(By.XPATH, locators.filling_button).click()
