from selenium import webdriver

chrome_driver_path = "C:\\Users\\USER\\Documents\\100DaysOfPython\\chromedriver.exe"

# instantiating a Chrome web driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# to launch the browser and open the website
driver.get("https://www.python.org")

# find element by id
nav_bar = driver.find_element_by_id("mainnav")
print(nav_bar.tag_name)

# find element by name
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

# find element by class
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

# find element by css selector
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

# find element by xpath
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# to close a tab
# driver.close()

# to close all tabs
driver.quit()
