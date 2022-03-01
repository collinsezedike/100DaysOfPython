from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver_path = "C:\\Users\\USER\\Documents\\100DaysOfPython\\chromedriver.exe"

service_obj = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.python.org")
dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events_dict = {}
for index in range(len(dates)):
    events_dict[index] = {
            "time": dates[index].text,
            "name": events[index].text
        }

pprint(events_dict)
driver.quit()
