from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2923865231&f_LF=f_AL&geoId=102257491&"
           "keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]").click()               # sign in button
time.sleep(5)
username_input = driver.find_element(By.ID, value="username")
username_input.send_keys("My username")
password_input = driver.find_element(By.ID, value="password")
password_input.send_keys("My password")
driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()           # sign in button
time.sleep(5)

gigs = driver.find_elements(By.CLASS_NAME, value="job-card-list__title")
for gig in gigs:
    gig.click()
    time.sleep(2)
    try:
        driver.find_element(By.CLASS_NAME, value="jobs-apply-button").click()
        apply_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
        # if the application does not require any input, go through with it, 
        # else quit applying and move on to the next application
        if apply_button.get_attribute("aria-label") == "Submit application":             
            apply_button.click()
        else:
            driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss").click()             # the x button
            time.sleep(2)
            driver.find_element(By.CLASS_NAME, value="artdeco-button--secondary").click()          # confirm application dismissal
    except NoSuchElementException:
        print("No application found")
