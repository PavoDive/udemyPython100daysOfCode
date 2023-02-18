from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.amazon.com/Secura-60-Minute-Mechanical-Countdown-Collapsible/dp/B0895S4NWP")

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
price = price.get_attribute("innerHTML")
price = float(price.replace("$", ""))

search_bar = driver.find_element(By.NAME, "field-keywords")


driver.close() # closes a tab
driver.quit() # closes the browser
