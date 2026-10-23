from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from selenium.common.exceptions import StaleElementReferenceException


class TestAdvertisement:
    def test_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        driver.find_element(*Locators.AD_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                                        presence_of_element_located(Locators.ERROR_POP_UP))

        assert driver.find_element(*Locators.ERROR_TEXT).text == 'Чтобы разместить объявление, авторизуйтесь'



    def test_ad_authorised(self, driver):
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

        driver.find_element(*Locators.AD_BUTTON).click()
        WebDriverWait(driver, 5, ignored_exceptions=(StaleElementReferenceException)).until(expected_conditions.
                                               presence_of_element_located(Locators.NEW_AD_TITLE))

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.AD_NAME)).send_keys("Товар")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.AD_DESCRIPTION)).send_keys("Тестовый товар")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.AD_PRICE)).send_keys("2999")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CATEGORY_ARROW)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CATEGORY_BOOKS)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CITY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CITY_MOSCOW)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.CONDITION_USED)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.PUBLISH_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://qa-desk.education-services.ru/"))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.USER_PIC)).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/profile"))
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.AD_CARD))

        assert driver.find_element(*Locators.AD_CARD).text == 'Товар'
