from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "../../chromedriver.exe"
service_obj = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")

five_sec = time.time() + 5
five_min = time.time() + 60*5

# one strategy I used is to put cookie.click() inside every loop
while five_min > time.time():
    cookie.click()

    # after five seconds
    if time.time() > five_sec:
        cookie.click()  # click the big cookie during these loops
        store = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        # convert the prices to integers
        store_prices_int = []
        for item in store:
            cookie.click()  # click the big cookie during these loops
            if item.text != "":
                price = item.text.split("-")[1].strip().replace(",", "")
                store_prices_int.append(int(price))

        # create a dictionary of cost and the div
        products_and_price = {}
        for index in range(len(store_prices_int)):
            cookie.click()  # click the big cookie during these loops
            products_and_price[store_prices_int[index]] = store[index]

        # get the amount of cookies you have and convert to a number
        amount = driver.find_element(By.ID, value="money")
        amount_int = int(amount.text.replace(",", ""))

        # buy a product in reversed order of cost
        for price in store_prices_int[::-1]:
            cookie.click()    # click the big cookie during these loops
            if amount_int >= price:
                product = products_and_price[price]
                product.click()
                break   # need to quit the loop otherwise, it will generate an error

        five_sec = time.time() + 5  

my_cps = driver.find_element(By.ID, value="cps")
print(my_cps.text)
driver.quit()

# Angela's
# from selenium import webdriver
# import time
#
# chrome_driver_path = "../../chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# # Get cookie to click on.
# cookie = driver.find_element_by_id("cookie")
#
# # Get upgrade item ids.
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# timeout = time.time() + 5
# five_min = time.time() + 60 * 5  # 5minutes
#
# while True:
#     cookie.click()
#
#     # Every 5 seconds:
#     if time.time() > timeout:
#
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements_by_css_selector("#store b")
#         item_prices = []
#
#         # Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element_by_id("money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element_by_id(to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break
