from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(chrome_driver_path)

SUPPOSED_SPEED = 200
INTERNET_PROVIDER = "MTNNG"


class InternetSpeedTwitterBot:

    def __init__(self):
        # configure pageLoadStrategy to none
        c = DesiredCapabilities.CHROME
        c["pageLoadStrategy"] = "none"
        self.driver = webdriver.Chrome(service=service_obj, desired_capabilities=c)
        self.download_speed = None
        self.upload_speed = None

    def get_internet_speed(self):
        w = WebDriverWait(self.driver, 30)
        self.driver.get("https://www.speedtest.net/")
        # wait till go button shows up
        w.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test")))
        # JavaScript Executor to stop page load
        time.sleep(20)
        self.driver.execute_script("window.stop();")
        self.driver.find_element(By.CLASS_NAME, value="js-start-test").click()  # click the go button
        time.sleep(60)
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
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(20)
        username_input = self.driver.find_element(By.NAME, value="text")
        username_input.send_keys("My username")
        username_input.send_keys(Keys.ENTER)
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys("My password")
        password_input.send_keys(Keys.ENTER)
        time.sleep(25)
        tweet_textarea = self.driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-block")
        tweet_textarea.click()
        tweet_textarea.send_keys(f"Hey @{INTERNET_PROVIDER}, why is my internet speed {self.download_speed}down/{self.upload_speed}"
                                 f"up when I pay for {SUPPOSED_SPEED}Mbps?")
        time.sleep(2)
        # tweet button
        self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span').click()
        print("Tweet sent!")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
