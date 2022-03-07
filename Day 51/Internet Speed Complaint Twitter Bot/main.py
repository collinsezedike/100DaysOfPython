from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(chrome_driver_path)

SUPPOSED_SPEED = 200
INTERNET_PROVIDER = "MTNNG"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service_obj)
        self.download_speed = None
        self.upload_speed = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, value="js-start-test").click()
        time.sleep(45)
        self.download_speed = float(self.driver.find_element(By.CSS_SELECTOR, value="span.download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CSS_SELECTOR, value="span.upload-speed").text)
        print(f"Your download speed is {self.download_speed}Mbps"
              f"\n and your upload speed is {self.upload_speed}Mbps")
        if self.download_speed < SUPPOSED_SPEED or self.upload_speed < SUPPOSED_SPEED:
            print("Tweeting to Internet Provider")
            self.tweet_at_provider()
        time.sleep(5)
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        phone_number_input = self.driver.find_element(By.NAME, value="text")
        phone_number_input.send_keys("email address")
        self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span').click()
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys("password")
        self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span').click()
        time.sleep(25)
        tweet_textarea = self.driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-block")
        tweet_textarea.click()
        tweet_textarea.send_keys(f"Hey @{INTERNET_PROVIDER}, why is my internet speed {self.download_speed}down/{self.upload_speed}"
                                 f"up when I pay for {SUPPOSED_SPEED}Mbps?")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
