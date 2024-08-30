import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_waits():
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)

    log_in_email_web_element =driver.find_element(By.XPATH,"//input[@id='login-username']")
    log_in_email_web_element.send_keys("admin@admin.com")


    log_in_password_web_element =driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    log_in_password_web_element.send_keys("admin")


    submit_button_element = driver.find_element(By.CSS_SELECTOR,"button[id='js-login-btn']")
    submit_button_element.click(   )
    

    WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((By.ID,"js-notification-box-msg"))
    )


    error_message_web_element = driver.find_element(By.XPATH,"//div[@id='js-notification-box-msg']")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    
    
