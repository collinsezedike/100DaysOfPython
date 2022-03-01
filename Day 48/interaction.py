from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/USER/Documents/100DaysOfPython/chromedriver.exe"

service_obj = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# to click on a link
article_count.click()

# a special method for finding links
all_portals = driver.find_element(By.LINK_TEXT, value="All portals")
all_portals.click()

# to type something
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
# to press enter
search.send_keys(Keys.ENTER)

# driver.quit()
