from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators import TestLocators
from conftest import generate_name, generate_password, generate_mail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSignup:
    def test_sign_up(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 6)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()


    def test_sign_up_incorrect_password(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 5)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//div/form/fieldset[3]/div/p[text() = 'Некорректный пароль']")))


