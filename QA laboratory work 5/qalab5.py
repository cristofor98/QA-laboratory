from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver 

driver = webdriver.Chrome('/Users/tekwill/Downloads/chromedriver')
driver.get("https://www.amazon.com/")
search_bar = driver.find_element_by_id("twotabsearchtextbox")
search_bar.clear()
search_bar.send_keys("computer")
search_bar.submit()
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers
        )
driver.close()

