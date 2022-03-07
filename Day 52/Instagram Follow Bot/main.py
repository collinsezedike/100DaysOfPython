from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

USERNAME = "username"
PASSWORD = "password"
TARGET_ACCOUNT = "python.hub"

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(chrome_driver_path)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service_obj)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, value="button.L3NKy").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, value="button.yWX7d").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, value="button.HoLwm").click()
        print("Login In Sucessful!")

    def find_followers(self):
        self.driver.get("https://www.instagram.com/{TARGET_ACCOUNT}/")
        self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(3)
        pop_up = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
        time.sleep(1)
        print("Followers Fetched")

    def follow(self):
        time.sleep(2)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for follow_button in buttons:
            follow_button.click()
            time.sleep(2)
        print("Followed!")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
