from selenium.webdriver.common.by import By

class TestLocators:
    #LOGIN_PAGE
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"
    EMAIL_FIELD_LOGIN = By.XPATH, ".//div/main/div/form/fieldset[1]/div/div/input"
    PASSWORD_FIELD_LOGIN = By.XPATH, ".//div/main/div/form/fieldset[2]/div/div/input"
    SIGNUP_LINK = By.XPATH, ".//div/p[1]/a[text() = 'Зарегистрироваться']"
    FORGOT_PASSWORD_LINK = By.XPATH, "*//div/div/p[2]/a"
    #MAIN_PAGE
    LOGIN_BUTTON_MAIN_PAGE = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    CLIENTS_AREA_BUTTON = By.XPATH, ".//div/header/nav/a/p[text() = 'Личный Кабинет']"
    KONSTRUCTOR_BUTTON = By.XPATH, ".//div/header/nav/ul/li[1]/a/p[text() = 'Конструктор']"
    BURGER_LOGO = By.XPATH, "./html/body/div/div/header/nav/div/a"
    BULKI_SECTION = By.XPATH, ".//div/main/section[1]/div[1]/div[1]/span[text() = 'Булки']"
    SOUSE_SECTION = By.XPATH, ".//div/main/section[1]/div[1]/div[2]/span[text() = 'Соусы']"
    FILLINGS_SECTION = By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span[text() = 'Начинки']"
    #SIGNUP_PAGE
    NAME_FIELD_SIGNUP = By.XPATH, ".//input[@name = 'name']"
    EMAIL_FIELD_SIGNUP = By.XPATH, ".//div/form/fieldset[2]/div/div/input"
    PASSWORD_FIELD_SIGNUP = By.XPATH, ".//div/form/fieldset[3]/div/div/input"
    REGISTRATION_BUTTON = By.XPATH, "//div/form/button[text() = 'Зарегистрироваться']"
    #PASSWORD_RECOVERY_PAGE
    EMAIL_RECOVERY_FIELD = By.XPATH, ".//input[@name = 'Name']"
    RECOVERY_FIELD = By.XPATH, ".//button[text() = 'Восстановить']"
    LOGIN_BUTTON_RECOVERY_PAGE = By.XPATH, ".//div/main/div/div/p/a[text() = 'Войти']"
    #CLIENTS_AREA
    LOGOUT_BUTTON = By.XPATH,".//button[contains(text(), 'Выход')]"

