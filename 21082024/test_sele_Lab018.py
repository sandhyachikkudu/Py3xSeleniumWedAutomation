import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_Action_builder_selenium():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold -> click and Hole, we will not release it.


    atag =driver.find_element(By.XPATH,"//a[@id='click']")
    atag.click()
    time.sleep(2)

    action_builder = ActionBuilder(driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()
    time.sleep(5)



