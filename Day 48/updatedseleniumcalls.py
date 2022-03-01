from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\USER\\Documents\\100DaysOfPython\\chromedriver.exe"

service_obj = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service_obj)

# to launch the browser and open the website
driver.get("https://www.python.org")

# find element by id
nav_bar = driver.find_element(By.ID, value="mainnav")
print(nav_bar.tag_name)

# find element by name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

# find element by class
logo = driver.find_element(By.CLASS_NAME, value="python-logo")
print(logo.size)

# find element by css selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# find element by xpath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# to close a tab
# driver.close()

# to close all tabs
driver.quit()
