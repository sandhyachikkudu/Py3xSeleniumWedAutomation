import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_login_VWO():
    chrome_option = Options()
    chrome_option.add_argument("--page-load-startegy=none")
    # chrome_option.add_argument("--page-load-startegy=normal")
    # chrome_option.add_argument("--page-load-startegy=eager")

    driver = webdriver.Chrome(chrome_option)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    