import password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self):
        """

        """
        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com")


    def login(self):
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span")
        login_button.click()
        
        username_box = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        username_box.send_keys(password.username + Keys.ENTER)
        passwd_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwd_box.send_keys(password.passwd + Keys.ENTER)

        # I got stuck from here, as it requires the input of a verification code and I'm not creating a new account on twitter, out of ethical concerns


    def send_message(self, message):
        text_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        script = f"arguments[0].innerText='{message}';"
        self.driver.execute_script(script, text_field)
        twit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
        twit_button.click()


    def close(self):
        self.driver.close()


