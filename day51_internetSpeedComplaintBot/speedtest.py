from selenium import webdriver
from selenium.webdriver.common.by import By
import time

speed_url = "https://www.speedtest.net/"



class SpeedTest:
    def __init__(self):
        """

        """
        self.download = 0
        self.upload = 0
        self.result_id = ""
        self.text = ""
        self.update()

        
    def update(self):
       driver = webdriver.Firefox()
       driver.get(speed_url)
       go_button = driver.find_element(By.CLASS_NAME, "js-start-test")
       go_button.click()

       time.sleep(20)
       result_download = driver.find_element(By.CLASS_NAME, "download-speed")
       self.download = float(result_download.text)

       result_upload = driver.find_element(By.CLASS_NAME, "upload-speed")
       self.upload = float(result_upload.text)

       result_id = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a")
       self.result_id = result_id.text


    def share_text(self, download_std):
        def compose_text(speed_txt):
            return f"Hi @emcali. Today's internet speed is very {speed_txt[0]}. I've got {self.download} Mbps in download and {self.upload} Mbps in upload, which is surely {speed_txt[1]} what you promised. {speed_txt[2]}"
        if self.download > 1.2 * download_std:
            speed_text = ["fast!", "above", "Keep the good job!"]
            return compose_text(speed_text)
        elif self.download < 0.8 * download_std:
            speed_text = ["slow!", "below", "Please do something about it!"]
            return compose_text(speed_text)


    def close(self):
        self.driver.close()



