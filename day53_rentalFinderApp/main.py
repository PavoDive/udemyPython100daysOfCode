from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

g_form ="https://docs.google.com/forms/d/e/1FAIpQLSfZBZStihhBaK3dImFPsG2_G1aYhm-3_i3hGVsPHrIo_KWxNA/viewform?usp=sf_link"

z_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Statesville%2C%20NC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.82109316131931%2C%22east%22%3A-79.82432802460056%2C%22south%22%3A35.18173994600505%2C%22north%22%3A36.10134025105988%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A300764%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1500%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%2C%22customRegionId%22%3A%2226c0a63f27X1-CRhuj3ew78i0g5_1cm82e%22%7D"

# response = requests.get(z_url)
# I'm crashing against a captcha :(

driver = webdriver.Firefox()
driver.get(z_url)

element_count = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[1]/div/span").text.split(" ")[0])

element_prices = driver.find_elements(By.CSS_SELECTOR, 'span[data-test="property-card-price"]')

while len(element_prices) < element_count:
    driver.execute_script("arguments[0].scrollIntoView();", element_prices[-1])
    time.sleep(4)
    element_prices = driver.find_elements(By.CSS_SELECTOR, 'span[data-test="property-card-price"]')

element_ps = [e.text for e in element_prices]

element_addresses = driver.find_elements(By.CSS_SELECTOR, 'address[data-test="property-card-addr"]')
element_adds = [e.text for e in element_addresses]

element_urls = driver.find_elements(By.CSS_SELECTOR, 'a[data-test="property-card-link"][tabindex="0"]')
element_links = [e.get_attribute("href") for e in element_urls]


# ---------------- Fill Forms ----------------
driver.get(g_form)

add_selector =   "div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
price_selector = "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
link_selector = "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

button_selector = ".Y5sE8d > span:nth-child(3) > span:nth-child(1)"

for i in range(len(element_prices)):
    a = driver.find_element(By.CSS_SELECTOR, add_selector)
    a.send_keys(element_adds[i])

    p = driver.find_element(By.CSS_SELECTOR, price_selector)
    p.send_keys(element_ps[i])

    l = driver.find_element(By.CSS_SELECTOR, link_selector)
    l.send_keys(element_links[i])

    b = driver.find_element(By.CSS_SELECTOR, button_selector)
    b.click()
    time.sleep(3)

    back_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    back_link.click()
    time.sleep(3)


driver.close()
