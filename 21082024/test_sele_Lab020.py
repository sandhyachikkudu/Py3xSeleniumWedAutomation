import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
def test_make_my_trip():
    load_dotenv()
    driver =webdriver.Chrome()

    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']"))
    )

    driver.find_element(By.XPATH,"//span[@class='commonModal__close']" ).click()

    fromCity = driver.find_element(By.XPATH,"//input[@data-cy='fromCity']")
    action =ActionChains(driver)
    # action.move_to_element(fromCity).click().send_keys("Mumbai").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    action.move_to_element(fromCity).click().send_keys(os.getenv("CITY")).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(10)