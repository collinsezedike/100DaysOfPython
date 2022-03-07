from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

PHONE_NUMBER = "phone number"
PASSWORD = "password"

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.tinder.com")
time.sleep(10)

# login button
driver.find_element(By.CSS_SELECTOR, value="a.button").click()
time.sleep(2)

# login with facebook button
driver.find_element(
    By.XPATH,
    value='//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]').click()
time.sleep(5)

tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]

# on the facebook login prompt
driver.switch_to.window(facebook_window)
driver.find_element(By.NAME, value="email").send_keys(PHONE_NUMBER)
driver.find_element(By.NAME, value="pass").send_keys(PASSWORD)
driver.find_element(By.NAME, value="login").click()
time.sleep(10)
driver.switch_to.window(tinder_window)
print("login successful!")
time.sleep(2)

# accept location
driver.find_element(By.XPATH, value='//*[@id="q1236064299"]/div/div/div/div/div[3]/button[1]/span').click()
print("Allowed location access.")
time.sleep(2)

# reject matches suggestions
driver.find_element(By.XPATH, value='//*[@id="q1236064299"]/div/div/div/div/div[3]/button[2]/span').click()
print("Rejected match suggestions.")
time.sleep(2)

# reject cookies
driver.find_element(By.XPATH, value='//*[@id="q-1330521921"]/div/div[2]/div/div/div[1]/div[2]/button/span').click()
print("Rejected cookies.")
time.sleep(10)
# accept cookies
# driver.find_element(By.XPATH, value='//*[@id="q-1330521921"]/div/div[2]/div/div/div[1]/div[1]/button/span').click()
i = 1
while i <= 20:
    try:
        buttons = driver.find_elements(By.XPATH, value="//span[contains(@class, 'D(b)')]")
        like_button = buttons[2]
        like_button.click()
    except ElementClickInterceptedException:
        try:
            # not interested in adding tinder to home screen
            driver.find_element(By.XPATH, value='//*[@id="q1236064299"]/div/div/div[2]/button[2]/span').click()
        except NoSuchElementException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
            except NoSuchElementException:
                time.sleep(2)
    print(f"Liked {i} person")
    i += 1
    time.sleep(2)

driver.quit()
