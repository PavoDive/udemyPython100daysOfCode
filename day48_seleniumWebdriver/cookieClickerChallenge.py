from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


start_time = int(time.time())
initial_time = 1

while (start_time + 300) > time.time():
    cookie.click()
    if int(time.time()) % int(initial_time) == 0:
        initial_time *= 1.05
        # if initial_time > 45:
        #     initial_time = 20
        store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div")
        highest_clickable_index = [i.get_attribute("class") for i in store_elements].index("grayed")
        if highest_clickable_index > 0:
            highest_clickable_index = highest_clickable_index - 1

            clickable_element = store_elements[highest_clickable_index]
            clickable_element.click()


cps = driver.find_element(By.ID, "cps")
print(cps.text)

driver.close()

