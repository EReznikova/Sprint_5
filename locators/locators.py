from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.buttonSecondary.inButtonText.undefined.inButtonText')
    REGISTRATION_POP_UP = (By.TAG_NAME, 'form')
    NO_ACCOUNT_BUTTON = (By.XPATH, "//form//button[normalize-space()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//form//button[normalize-space()='Создать аккаунт']")
    PROFILE_NAME = (By.CSS_SELECTOR, '.profileText.name')
    USER_PIC = (By.CLASS_NAME, "circleSmall")
    ERROR_MESSAGE = (By.CLASS_NAME, 'input_span__yWPqB')

    EMAIL_ERROR = (By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]")
    PASSWORD_ERROR = (By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]")
    REPEAT_PASSWORD_ERROR = (By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]")

    LOGIN_BUTTON = (By.XPATH, "//form//button[normalize-space()='Войти']")
    EXIT_BUTTON = (By.CSS_SELECTOR, '.spanGlobal.btnSmall')

    AD_BUTTON =  (By.XPATH, "//button[normalize-space()='Разместить объявление']")

    ERROR_POP_UP = (By.CSS_SELECTOR, '.popUp_shell__LuyqR')
    ERROR_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')

    NEW_AD_TITLE = (By.CSS_SELECTOR, ".hi.createListing_title__IFtFs")
    AD_NAME = (By.NAME, "name")
    AD_DESCRIPTION = (By.CSS_SELECTOR, "textarea[name='description']")
    AD_PRICE = (By.NAME, "price")
    CATEGORY_ARROW = (By.CSS_SELECTOR,"input[name='category'] + button")
    CATEGORY_BOOKS = (By.XPATH,"//span[normalize-space()='Книги']/parent::button")
    CITY_DROPDOWN = (By.CSS_SELECTOR,"input[name='city'] + button")
    CITY_MOSCOW = (By.XPATH,"//span[normalize-space()='Москва']/parent::button")
    CONDITION_USED = (By.XPATH,"//input[@name='condition' and @value='Б/У']/parent::div")
    PUBLISH_BUTTON = (By.XPATH,"//button[normalize-space()='Опубликовать']")
    PROFILE_TITLE = (By.CSS_SELECTOR, ".h1.zeroMargin")
    AD_CARD = (By.XPATH,"//*[normalize-space()='Товар']")