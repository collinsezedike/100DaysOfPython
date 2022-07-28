import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

X_COR = 360
Y_COR = 420
COLOR = (83, 83, 83)

chrome_driver_path = "./chromedriver.exe"
service_obj = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("https://elgoog.im/t-rex/")
driver.find_element(By.CSS_SELECTOR, value="body").send_keys(Keys.UP) # starts the game once the page has loaded

while True:
    s = pyautogui.screenshot()
    if s.getpixel((X_COR, Y_COR)) == COLOR or s.getpixel((X_COR, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR, Y_COR+20)) == COLOR or s.getpixel((X_COR, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+10, Y_COR)) == COLOR or s.getpixel((X_COR+10, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+10, Y_COR+20)) == COLOR or s.getpixel((X_COR+10, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+20, Y_COR)) == COLOR or s.getpixel((X_COR+20, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+20, Y_COR+20)) == COLOR or s.getpixel((X_COR+20, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+30, Y_COR)) == COLOR or s.getpixel((X_COR+30, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+30, Y_COR+20)) == COLOR or s.getpixel((X_COR+30, Y_COR+30)) == COLOR:
        pyautogui.keyDown("up")
        # I don't use the driver to make gameplay actions because 
        # the driver is dependent on network unlike pyautogui 
        
    # to restart after failing
    if s.getpixel((513,413)) == COLOR:
        print("Starting a new game...")
        pyautogui.keyUp("up")
