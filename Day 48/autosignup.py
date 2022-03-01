from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C://Users/USER/Documents/100DaysOfPython/chromedriver.exe"
service_obj = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name_input = driver.find_element(By.NAME, value="fName")
f_name_input.send_keys("My First Name")
l_name_input = driver.find_element(By.NAME, value="lName")
l_name_input.send_keys("My Last Name")
email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("myemailaddress@email.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()
