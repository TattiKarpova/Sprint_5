import pytest
import string
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from date import BASE_URL

from locators import TestLocators


def generate_mail(self, length):
    all_symbols = string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    mail = f'{result}@mail.ru'
    return mail


def generate_name(self, length):
    all_symbols = string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    name = f'{result}'
    return name

def generate_password(self, length):
    all_symbols = string.ascii_lowercase
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    password = f'{result}'
    return password

@pytest.fixture

def driver():
    options = Options()

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Неявное ожидание элементов на странице
    driver.get(BASE_URL)
    yield driver

    driver.quit()





