from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from selenium.common.exceptions import StaleElementReferenceException


class TestLogin:
    def test_login(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                                presence_of_element_located(Locators.REGISTRATION_POP_UP))

        WebDriverWait(driver, 5, ignored_exceptions=(StaleElementReferenceException)).until(expected_conditions.
                                       element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys("ice553@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()


        WebDriverWait(driver, 5).until(expected_conditions.
                                               presence_of_element_located(Locators.PROFILE_NAME))

        assert driver.find_element(*Locators.PROFILE_NAME).text == "User." and driver.find_element(*Locators.USER_PIC).is_displayed()
