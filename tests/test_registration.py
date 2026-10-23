import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from selenium.common.exceptions import StaleElementReferenceException

def fill_field(driver, locator, value):
    def type_value(browser):
        field = browser.find_element(*locator)
        field.clear()
        field.send_keys(value)
        return field.get_attribute("value") == value

    WebDriverWait(
        driver,
        5,
        ignored_exceptions=(StaleElementReferenceException,)
    ).until(type_value)

class TestRegistrationPage:
    def test_registration(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.REGISTRATION_POP_UP))

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/regiatration"))

        fill_field(driver,Locators.EMAIL_INPUT,f"user{random.randint(100, 9999)}@ya.ru")
        fill_field(driver, Locators.PASSWORD_INPUT, "123456")
        fill_field(driver, Locators.REPEAT_PASSWORD_INPUT, "123456")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.PROFILE_NAME))

        assert driver.find_element(*Locators.PROFILE_NAME).text == "User." and driver.find_element(*Locators.USER_PIC).is_displayed()


    def test_registration_with_invalid_email(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.REGISTRATION_POP_UP))

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/regiatration"))

        fill_field(driver, Locators.EMAIL_INPUT, "неверно")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.ERROR_MESSAGE))

        assert driver.find_element(*Locators.ERROR_MESSAGE).text == "Ошибка" and driver.find_element(*Locators.EMAIL_ERROR).is_displayed() is True and driver.find_element(*Locators.PASSWORD_ERROR).is_displayed() is True and driver.find_element(*Locators.REPEAT_PASSWORD_ERROR).is_displayed() is True


    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.REGISTRATION_POP_UP))

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/regiatration"))

        fill_field(driver, Locators.EMAIL_INPUT, "ice553@ya.ru")
        fill_field(driver, Locators.PASSWORD_INPUT, "123456")
        fill_field(driver, Locators.REPEAT_PASSWORD_INPUT, "123456")

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON)).click()


        WebDriverWait(driver, 5).until(expected_conditions.
                                       presence_of_element_located(Locators.ERROR_MESSAGE))

        assert driver.find_element(*Locators.ERROR_MESSAGE).text == "Ошибка" and driver.find_element(*Locators.EMAIL_ERROR).is_displayed() is True and driver.find_element(*Locators.PASSWORD_ERROR).is_displayed() is True and driver.find_element(*Locators.REPEAT_PASSWORD_ERROR).is_displayed() is True
