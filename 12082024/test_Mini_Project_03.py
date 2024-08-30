

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
@pytest.mark.positive
@allure.title("Signin to IDrive 360 website anc check upgrade - test_mini_project_3")
@allure.description("Verify that user able to sign in IDrive 360 website and can click on upgrade button")
def test_task_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    assert driver.current_url == "https://www.idrive360.com/enterprise/login"
    time.sleep(5)

    email_web_element = driver.find_element(By.ID,"username")
    email_web_element.send_keys("augtest_040823@idrive.com")
    time.sleep(5)

    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys("123456")
    time.sleep(5)

    signin_button_element = driver.find_element(By.ID, "frm-btn")
    signin_button_element.click()

    time.sleep(15)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    upgrade_now = driver.find_element(By.XPATH,"//span[contains(text(),'free')]")
    assert upgrade_now.text == "Your free trial has expired"

    allure.attach(driver.get_screenshot_as_png(), name='upgrade_screenshot')
    time.sleep(3)
    driver.quit()
    
