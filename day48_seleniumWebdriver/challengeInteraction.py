from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

wiki_pages = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(wiki_pages.text)

# wiki_pages.click()

# this is another, convenient way to search for links:
wikibooks = driver.find_element(By.LINK_TEXT, "Wikibooks")

# wikibooks.click()

# inputting text:
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)

driver.close()
