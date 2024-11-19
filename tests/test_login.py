from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators import TestLocators
from conftest import generate_name, generate_password, generate_mail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogIn:
    def test_log_in_on_main_page(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 6)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.BURGER_LOGO).click()
        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((TestLocators.CLIENTS_AREA_BUTTON)))

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()

        actualEmail = driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute('Value')
        assert email == actualEmail

    def test_log_in_on_ca(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 6)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.BURGER_LOGO).click()

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((TestLocators.CLIENTS_AREA_BUTTON)))

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()

        actualEmail = driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute('Value')
        assert email == actualEmail

    def test_log_in_on_reg_page(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 6)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((TestLocators.CLIENTS_AREA_BUTTON)))

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()

        actualEmail = driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute('Value')
        assert email == actualEmail


    def test_log_in_on_recovery_page(self, driver):
        name = generate_name(self, 6)
        email = generate_mail(self, 6)
        password = generate_password(self, 6)

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()
        driver.find_element(*TestLocators.SIGNUP_LINK).click()
        driver.find_element(*TestLocators.NAME_FIELD_SIGNUP).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_SIGNUP).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_SIGNUP).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*TestLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*TestLocators.LOGIN_BUTTON_RECOVERY_PAGE).click()

        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((TestLocators.CLIENTS_AREA_BUTTON)))

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()

        actualEmail = driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute('Value')
        assert email == actualEmail