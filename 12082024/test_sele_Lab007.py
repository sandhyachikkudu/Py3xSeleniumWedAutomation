import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_vwo_login():
   driver = webdriver.Chrome()
   driver.get("https://app.vwo.com")
   driver.refresh()
   anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free")
   anchor_tag_element.click()


   assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
   time.sleep(5)
   driver.quit()

   

