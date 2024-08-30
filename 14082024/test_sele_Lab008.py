import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Verify the error in app.VWO.com")
@allure.description("Verify the error while  log in toapp.VWO.com")
@pytest.mark.negative
def test_min_project_02():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    

    log_in_email_web_element =driver.find_element(By.XPATH,"//input[@id='login-username']")
    log_in_email_web_element.send_keys("admin@admin.com")


    log_in_password_web_element =driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    log_in_password_web_element.send_keys("admin123")


    submit_button_element = driver.find_element(By.CSS_SELECTOR,"button[id='js-login-btn']")
    submit_button_element.click(   )
    time.sleep(5)

    error_message_web_element = driver.find_element(By.XPATH,"//div[@id='js-notification-box-msg']")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    
    time.sleep(3)
    driver.quit()



    






























# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


# def test_vwo_login():
#    driver = webdriver.Chrome()
#    driver.get("https://app.vwo.com")
#    driver.refresh()
#    anchor_tag_element = driver.find_element(By.XPATH,"//input[@id='login-username']")
#    anchor_tag_element.send_keys("")


   

   

