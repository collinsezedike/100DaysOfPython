import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(chrome_driver_path)


class FormFiller:
    def __init__(self, form_url):
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.get(form_url)

    def fill_form(self, house_data: dict):
        all_inputs = self.driver.find_elements(By.CSS_SELECTOR, value="div.Xb9hP input")
        address_input = all_inputs[0]
        price_input = all_inputs[1]
        link_input = all_inputs[2]
        address_input.send_keys(house_data["address"])
        price_input.send_keys(house_data["price"])
        link_input.send_keys(house_data["link"])
        time.sleep(2)
        self.submit_form()

    def submit_form(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, value="span.RveJvd")
        submit_button.click()
        time.sleep(2)
        # to submit another response
        self.driver.find_element(By.CSS_SELECTOR, value="div.c2gzEf a").click()
