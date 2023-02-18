from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.python.org")

upcoming_events = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
upcoming_events_list = [event.text for event in upcoming_events]

desired_output = {i:{"time": upcoming_events_list[i].split("\n")[0], "event": upcoming_events_list[i].split("\n")[1]} for i in range(len(upcoming_events_list))}
