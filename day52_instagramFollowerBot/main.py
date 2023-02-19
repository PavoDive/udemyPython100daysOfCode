import password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

IG_TARGET_ACCOUNT = "nchealthnews"
# IG_TARGET_ACCOUNT = "n.c.child"

driver = webdriver.Firefox()

driver.get("https://www.instagram.com")
user_box = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
user_box.send_keys(password.username + Keys.ENTER)

pass_box = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
pass_box.send_keys(password.password + Keys.ENTER)

time.sleep(5)
not_now = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
not_now.click()

not_now_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
not_now_2.click()

new_url = f"https://www.instagram.com/{IG_TARGET_ACCOUNT}/followers/"
driver.get(new_url)

follower_count = int(driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span").text)

# scrolls the list of users until it gets to the end
reference_button = driver.find_element(By.CSS_SELECTOR, "div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._abcm div._aano div div div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm button")

for i in range(1, math.ceil(follower_count / 10)):
    reference_button.send_keys(Keys.END)
    time.sleep(5)
# scroll to top again!
driver.execute_script("arguments[0].scrollIntoView();", reference_button)

# find follow buttons
follow_buttons = driver.find_elements(By.CSS_SELECTOR, "div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._abcm div._aano div div div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm div._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0._abcm button")

counter = 1
for button in follow_buttons:
    if button.text == "Following" or button.text == "Requested":
        next
    else:
        button.click()
        time.sleep(3)
        counter += 1

    if counter % 15 == 0:
        print("Waiting 4 minutes to avoid exceeding insta limit")
        time.sleep(240)


