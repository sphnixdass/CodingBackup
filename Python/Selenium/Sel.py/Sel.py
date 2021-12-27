import logging
import sys
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import time

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.NOTSET)

url = "http://127.0.0.1:3010"


# driver = webdriver.Remote(command_executor=url,desired_capabilities={})
# driver.close()
# driver.session_id = "d918c95e-d7e3-4039-b8b2-49eaa4c452d0"
# create webdriver object
driver = webdriver.Chrome('./chromedriver',port=3010)
# get google.co.in
driver.get("https://google.co.in")
driver.get("https://google.co.in")
driver.get("https://google.co.in")
driver.get("https://google.co.in")
driver.get("https://google.co.in")
driver.get("https://google.co.in")
driver.get("https://google.co.in")

print(driver.command_executor._url)
print(driver.session_id)
# time.sleep(35)
# driver.get("https://google.co.in")
# time.sleep(35)
# driver.get("https://google.co.in")
# time.sleep(35)
# driver.get("https://google.co.in")
# time.sleep(35)
# driver.get("https://google.co.in")
# time.sleep(35)
driver.quit()

