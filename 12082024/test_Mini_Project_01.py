import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Verify the changes in URL")
@allure.description("Verify the changes in URL  by clicking on the make appointment button")
@pytest.mark.positive
def test_min_project_01():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    


   
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()
    time.sleep(5)