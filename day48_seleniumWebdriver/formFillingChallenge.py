from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Gio")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Pavo"+Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("any@wherever.com")

send = driver.find_element(By.TAG_NAME, "button")
send.click()


# The page doesn't send me to a "success" web page, because it is an archived version. The original one was down:
#  Application error

# An error occurred in the application and your page could not be served. If you are the application owner, check your logs for details. You can do this from the Heroku CLI with the command
# heroku logs --tail

driver.close()
