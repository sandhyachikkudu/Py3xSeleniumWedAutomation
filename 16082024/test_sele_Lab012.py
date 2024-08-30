import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


@allure.title("Verify the log in to URL")
@allure.description("Verify the log in to URL  by clicking on the make appointment button and message make appointment ")
@pytest.mark.positive
def test_min_project_01():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    
    WebDriverWait(driver=driver,timeout=5).until(
        EC.url_contains("profile.php#login")
    )


    log_in_email_web_element =driver.find_element(By.NAME,"username")
    log_in_email_web_element.send_keys("John Doe")


    log_in_password_web_element =driver.find_element(By.ID,"txt-password")
    log_in_password_web_element.send_keys("ThisIsNotAPassword")


    submit_button_element = driver.find_element(By.ID,"btn-login")
    submit_button_element.click( )

    ignore_list =[ElementNotVisibleException,ElementNotSelectableException]

    WebDriverWait(driver=driver,timeout=5,poll_frequency=1,ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[class='col-sm-12 text-center']"))
    )

    message_web_element = driver.find_element(By.CSS_SELECTOR,"[class='col-sm-12 text-center']")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    assert message_web_element.text=="Make Appointment"

