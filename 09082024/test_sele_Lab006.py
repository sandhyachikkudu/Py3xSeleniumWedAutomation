import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_vwo_login():
   driver = webdriver.Chrome()
   driver.get("https://app.vwo.com")
   driver.refresh()
#    driver.back()
#    driver.forward()
   

#    driver.close()
# time.sleep(10)
# close will close the current window or tab
# session id != null(invalid)
   time.sleep(10)
   driver.quit()

#    close will close  allthe  window or tab
# session id == null(invalid)
   time.sleep(10)