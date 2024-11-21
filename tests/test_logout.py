import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import requests

from conftest import driver
from locators import TestLocators
from conftest import generate_name, generate_password, generate_mail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogOut:
    def test_log_out(self, driver):
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

        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((TestLocators.CLIENTS_AREA_BUTTON)))

        driver.find_element(*TestLocators.CLIENTS_AREA_BUTTON).click()

        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()


        response = requests.get("https://stellarburgers.nomoreparties.site/api/auth/logout")

        # Проверяем статус ответа
        assert response.status_code == 200





