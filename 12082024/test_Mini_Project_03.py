import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Verify the error in app.VWO.com")
@allure.description("Verify the error while  log in toapp.VWO.com")
@pytest.mark.positive
def test_min_project_02():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    email_web_element = driver.find_element(By.NAME,"username")
    email_web_element.send_keys("augtest_040823@idrive.com")


    password_web_element = driver.find_element(By.CSS_SELECTOR,"[tabindex='0']")
    password_web_element.send_keys("123456")
    

    submit_web_element = driver.find_element(By.ID,"frm-btn")
    submit_web_element.click()
    time.sleep(3)

    upgrade_message_element =driver.find_element(By.XPATH,"//div[@id='upgrade']/span")
    time.sleep(3)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    assert upgrade_message_element.text == "Your free trial has expired"
    time.sleep(5)
 
    
