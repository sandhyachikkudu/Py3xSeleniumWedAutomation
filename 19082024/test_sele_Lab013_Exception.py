import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def test_VWO_login():
    driver =webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element=driver.find_element(By.ID,"this_id_doesnotexist")

    except NoSuchElementException:
        print("Element not found")

    print("end of program")