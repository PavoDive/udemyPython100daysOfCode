from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from PIL import Image

service = Service(log_path = "log.log")
driver = webdriver.Firefox(service = service)
driver.get("https://elgoog.im/dinosaur-game/")

# start game
# find screen
main_content = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/canvas')
main_content.click()
driver.keys(Keys.SPACE)
