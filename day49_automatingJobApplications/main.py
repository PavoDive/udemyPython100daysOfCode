from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as se
import time
import password

url = "https://www.linkedin.com/jobs/search/?keywords=director%20de%20manufactura&location=Valle%20del%20Cauca%2C%20Colombia"

driver = webdriver.Firefox()

driver.get(url)

sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(password.user + Keys.ENTER)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password.psswd + Keys.ENTER)

job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")

for job_card in job_cards:
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", job_card)
    job_card.click()

    follow_btn = driver.find_elements(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/section/section/div[1]/div[1]/button/span")
    if len(follow_btn) == 0:
        next
    else:
        driver.execute_script("arguments[0].scrollIntoView();", follow_btn[0])
        follow_btn[0].click()
        

driver.close()

